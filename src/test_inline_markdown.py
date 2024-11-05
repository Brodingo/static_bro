import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TextSplitNodesDelimiter(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes,result_nodes)

    def test_extract_markdown_images(self):
        text = "here is my ![image one](image1.jpg)"
        result = extract_markdown_images(text)
        images = [("image one", "image1.jpg")]
        self.assertListEqual(
            result,
            images
        )

    def test_extract_markdown_images_multiple(self):
        text = "here is my ![image one](image1.jpg) and then my ![image two](image2.jpg)"
        result = extract_markdown_images(text)
        images = [("image one", "image1.jpg"),("image two", "image2.jpg")]
        self.assertListEqual(
            result,
            images
        )

    def test_extract_markdown_images_with_link(self):
        text = "here is my ![image one](image1.jpg) and then my link [image two](image2.jpg)"
        result = extract_markdown_images(text)
        images = [("image one", "image1.jpg")]
        self.assertListEqual(
            result,
            images
        )

    def test_extract_markdown_links(self):
        text = "here is my link [image one](image1.jpg)"
        result = extract_markdown_links(text)
        links = [("image one", "image1.jpg")]
        self.assertListEqual(
            result,
            links
        )

    def test_extract_markdown_links_mutiple(self):
        text = "here is my link [image one](image1.jpg) and then my other link [image two](image2.jpg)"
        result = extract_markdown_links(text)
        links = [("image one", "image1.jpg"), ("image two", "image2.jpg")]
        self.assertListEqual(
            result,
            links
        )

    def test_extract_markdown_links_wit_image(self):
        text = "here is my link [image one](image1.jpg) and then my image ![image two](image2.jpg)"
        result = extract_markdown_links(text)
        links = [("image one", "image1.jpg")]
        self.assertListEqual(
            result,
            links
        )

if __name__ == "__main__":
    unittest.main()