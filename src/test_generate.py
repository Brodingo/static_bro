import unittest

from generate import extract_title


class TestGenerate(unittest.TestCase):
    def test_extract_title(self):
        markdown = (
            "# This is a heading\n"
            "\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        )
        result = extract_title(markdown)
        self.assertEqual(
            result,
            "This is a heading"
        )
