"""Validate the published PM skill collection without private research inputs."""
import json
from pathlib import Path
import re
import subprocess
import sys

from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'agent-workflow', 'ai-product-bets', 'ai-prototype', 'b2b-sales', 'career',
    'craft-review', 'customer-interviews', 'decide', 'eval-plan', 'exec-comms',
    'experiment', 'growth-model', 'hard-conversations', 'hire', 'influence',
    'launch', 'metrics', 'pmf-check', 'position', 'price', 'prioritize',
    'ship-faster', 'spec', 'strategy', 'validate-idea',
}
REQUIRED_SECTIONS = ['Step 1', 'Step 2', 'Step 3', 'Where the experts disagree']


def main():
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    skill_paths = sorted((ROOT / 'skills').glob('*/SKILL.md'))
    actual = {p.parent.name for p in skill_paths}
    check(actual == EXPECTED, f'Skill inventory mismatch: missing {EXPECTED-actual}, extra {actual-EXPECTED}')
    for path in skill_paths:
        slug = path.parent.name
        text = path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        try:
            check(text.startswith('---\n') and len(parts) == 3, f'{slug}: missing frontmatter')
            metadata = yaml.safe_load(parts[1])
            check(metadata.get('name') == slug, f'{slug}: frontmatter name mismatch')
            description = metadata.get('description')
            check(isinstance(description, str) and 1 <= len(description) <= 1024,
                  f'{slug}: missing or overlong description')
        except (yaml.YAMLError, AttributeError, IndexError) as error:
            errors.append(f'{slug}: invalid frontmatter: {error}')
        for section in REQUIRED_SECTIONS:
            check(section in text, f'{slug}: missing {section}')
        check('rubric' in text.lower() or 'grade' in text.lower(), f'{slug}: missing grading guidance')
        for filename in ['references/frameworks.md', 'references/quotes.md', 'assets/card.png']:
            check((path.parent / filename).is_file(), f'{slug}: missing {filename}')
        card = path.parent / 'assets/card.png'
        if card.exists():
            try:
                with Image.open(card) as image:
                    check(image.format == 'PNG', f'{slug}: card is not PNG')
                    check(image.width * 4 == image.height * 3, f'{slug}: card ratio is not 3:4')
                    image.verify()
            except (OSError, SyntaxError) as error:
                errors.append(f'{slug}: invalid image: {error}')
        check('(assets/card.png)' in text, f'{slug}: image is not attached')

    # Check local targets in published documentation, ignoring example code blocks.
    docs = [ROOT / name for name in ['README.md', 'QUICKSTART.md', 'SKILLS-INDEX.md',
                                    'CONTRIBUTING.md', 'CHANGELOG.md', 'images/README.md']]
    docs += list((ROOT / 'docs').rglob('*.md')) + list((ROOT / 'skills').rglob('*.md'))
    docs += list((ROOT / 'extras').rglob('*.md'))
    for path in docs:
        if not path.is_file():
            errors.append(f'Missing documentation: {path.relative_to(ROOT)}')
            continue
        text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
        targets = re.findall(r'!?\[[^\]\n]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)', text)
        targets += re.findall(r'(?:href|src)="([^"]+)"', text)
        for target in targets:
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            local = target.split('#', 1)[0].strip('<>')
            if local:
                destination = (path.parent / local).resolve()
                check(destination.exists(), f'{path.relative_to(ROOT)}: broken link {target}')
                check(not destination.is_relative_to(ROOT / 'images/refs'),
                      f'{path.relative_to(ROOT)}: links to private headshots')

    try:
        plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        check(plugin['name'] == 'awesome-pm-skills', 'Unexpected plugin name')
        check(plugin['version'] == '2.0.0', 'Unexpected plugin version')
        check(plugin['license'] == 'MIT' and (ROOT / 'LICENSE').exists(), 'License missing or inconsistent')
        check(len(market['plugins']) == 1, 'Marketplace must contain the core collection once')
        entry = market['plugins'][0]
        check(entry['name'] == plugin['name'], 'Plugin and marketplace names differ')
        check(entry['version'] == plugin['version'], 'Plugin and marketplace versions differ')
        check(entry['source'] == './', 'Marketplace plugin path must be repository root')
        manifest = json.loads((ROOT / 'images/generation-manifest.json').read_text())
        check(len(manifest['cards']) == len(EXPECTED), 'Card manifest has duplicate or missing entries')
        check({c['skill'] for c in manifest['cards']} == EXPECTED, 'Card manifest inventory mismatch')
        for card in manifest['cards']:
            asset = (ROOT / 'images' / card['path']).resolve()
            check(asset == ROOT / 'skills' / card['skill'] / 'assets/card.png',
                  f"{card['skill']}: wrong manifest image path")
            if asset.exists():
                with Image.open(asset) as image:
                    check(list(image.size) == card['actual_size'], f"{card['skill']}: manifest dimensions differ")
    except (KeyError, ValueError, OSError) as error:
        errors.append(f'Invalid metadata: {error}')

    readme = (ROOT / 'README.md').read_text()
    index = (ROOT / 'SKILLS-INDEX.md').read_text()
    gallery = (ROOT / 'images/README.md').read_text()
    for slug in EXPECTED:
        check(f'(skills/{slug}' in readme, f'{slug}: missing from README')
        check(f'(skills/{slug}' in index, f'{slug}: missing from index')
        check(f'../skills/{slug}/assets/card.png' in gallery, f'{slug}: missing from gallery')
    forbidden = ('images/refs/', 'transcripts/', 'digests/', 'HEADSHOTS.md', 'SKILL_AUTHORING.md')
    tracked = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True)
    if tracked.returncode == 0:
        files = tracked.stdout.decode().split('\0')
        for filename in files:
            check(not filename.startswith(forbidden), f'Private/local input tracked: {filename}')
        ignored = subprocess.run(['git', 'check-ignore', '--no-index', '--stdin'], cwd=ROOT,
                                 input='images/refs/sample.jpg\ntranscripts/sample.txt\ndigests/sample.md\n',
                                 text=True, capture_output=True)
        check(len(ignored.stdout.splitlines()) == 3, 'Private inputs are not all excluded by .gitignore')
    for error in errors:
        print(f'ERROR: {error}')
    if errors:
        print(f'Validation failed: {len(errors)} issue(s)')
        return 1
    print(f'OK: {len(actual)} skills, references, illustrations, local links, plugin metadata, and private-input exclusions')
    return 0


if __name__ == '__main__':
    sys.exit(main())
