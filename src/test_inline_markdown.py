import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)


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

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        split_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertListEqual(
            new_nodes,
            split_nodes
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![image one](image1.jpg) and ![image two](image2.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        split_nodes = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("image one", TextType.IMAGE, "image1.jpg"),
            TextNode(" and ", TextType.TEXT),
            TextNode("image two", TextType.IMAGE, "image2.jpg"),
        ]
        self.assertListEqual(
            new_nodes,
            split_nodes
        )

if __name__ == "__main__":
    unittest.main()