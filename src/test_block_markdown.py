import unittest

from block_markdown import markdown_to_blocks, block_to_block_type

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = (
            "# This is a heading\n"
            "\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
            "\n"
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        )
        result = markdown_to_blocks(markdown)
        blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            (
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
            )
        ]
        self.assertListEqual(
            result,
            blocks
        )

    def test_block_to_block_type_heading(self):
        markdown = "### This is a heading"
        result = block_to_block_type(markdown)
        self.assertEqual(
            result,
            'heading'
        )

    def test_block_to_block_type_code(self):
        markdown = "``` This is a some code ```"
        result = block_to_block_type(markdown)
        self.assertEqual(
            result,
            'code'
        )

    def test_block_to_block_type_quote(self):
        markdown = (
            ">Fear is the mind killer\n"
            ">You'll all float down here\n"
            ">We're gonna need a bigger boat"
        )
        result = block_to_block_type(markdown)
        self.assertEqual(
            result,
            'quote'
        )

    def test_block_to_block_type_bad_quote(self):
        markdown = (
            ">Fear is the mind killer\n"
            ">You'll all float down here\n"
            "We're gonna need a bigger boat"
        )
        result = block_to_block_type(markdown)
        self.assertEqual(
            result,
            'paragraph'
        )

    def test_block_to_block_type_ul(self):
        markdown = (
            "* Good morning class\n"
            "* To the bus!\n"
            "* Please don't sue"
        )
        result = block_to_block_type(markdown)
        self.assertEqual(
            result,
            'unordered_list'
        )

    def test_block_to_block_type_ol(self):
        markdown = (
            "1. We gotta get jobs\n"
            "2. Then we get the khakis\n"
            "3. Then we get the chicks"
        )
        result = block_to_block_type(markdown)
        self.assertEqual(
            result,
            'ordered_list'
        )

    def test_block_to_block_type_paragraph(self):
        markdown = (
            "Yes hello this is dog\n"
            "Hi dog this is dad\n"
            "Hi dad bark bark"
        )
        result = block_to_block_type(markdown)
        self.assertEqual(
            result,
            'paragraph'
        )

