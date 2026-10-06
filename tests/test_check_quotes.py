"""Regression checks for false-positive and false-success quote verification."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from check_quotes import main, matches, norm


class QuoteMatchingTests(unittest.TestCase):
    def test_common_punctuation_and_whitespace(self):
        self.assertTrue(matches('We’re going — quickly — to learn today.',
                                [norm("we're going - quickly - to\nlearn today.")]))

    def test_fragments_must_share_a_transcript_and_order(self):
        quote = 'first fragment ... second fragment'
        self.assertFalse(matches(quote, ['first fragment', 'second fragment']))
        self.assertFalse(matches(quote, ['second fragment then first fragment']))
        self.assertTrue(matches(quote, ['first fragment some omitted text second fragment']))

    def test_short_fragments_are_not_ignored(self):
        self.assertFalse(matches('never said ... this longer passage really was quoted here',
                                 ['this longer passage really was quoted here']))

    def run_fixture(self, transcript, document):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            corpus = root / 'corpus'
            corpus.mkdir()
            if transcript is not None:
                (corpus / 'guest.txt').write_text(transcript)
            skill = root / 'skill.md'
            skill.write_text(document)
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                return main([str(skill), '--transcripts', str(corpus)])

    def test_unmatched_quote_returns_failure(self):
        self.assertEqual(self.run_fixture('a completely unrelated transcript',
                                         '"This quote does not exist in the transcript."'), 1)

    def test_no_quoted_passages_cannot_pass(self):
        self.assertEqual(self.run_fixture('a real nonempty transcript', 'No quotes here.'), 1)

    def test_empty_corpus_is_rejected(self):
        with self.assertRaises(SystemExit) as result:
            self.run_fixture(None, '"Here is a sufficiently long quoted passage."')
        self.assertEqual(result.exception.code, 2)

    def test_verified_quote_returns_success(self):
        self.assertEqual(self.run_fixture('Here is a sufficiently long quoted passage.',
                                         '"Here is a sufficiently long quoted passage."'), 0)


if __name__ == '__main__':
    unittest.main()
