import unittest

from htmlnode import HTMLNode, ParentNode
from textnode import TextNode, TextType
from markdown_html import block_to_html_node, markdown_to_html_node

class TestMarkdownHTML(unittest.TestCase):
    def test_block_to_html_node_quote(self):
        block = ">Flash"
        result = block_to_html_node(block, 'quote')
        node = ParentNode('blockquote', [HTMLNode(None, "Flash")])
        self.assertEqual(
            result.__repr__(), 
            node.__repr__()
        )

    def test_markdown_to_html_node_ul(self):
        markdown = (
            "* Thing 1\n"
            "* Thing 2"
        )
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        html = '<div><ul><li>Thing 1</li><li>Thing 2</li></ul></div>'
        self.assertEqual(
           result,
           html
        )

    def test_markdown_to_html_node_ol(self):
        markdown = (
            "1. Thing 1\n"
            "2. Thing 2"
        )
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        html = '<div><ol><li>Thing 1</li><li>Thing 2</li></ol></div>'
        self.assertEqual(
           result,
           html
        )

    def test_markdown_to_html_node_code(self):
        markdown = "```python```"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        html = '<div><pre><code>python</code></pre></div>'
        self.assertEqual(
           result,
           html
        )

    def test_markdown_to_html_node_h3(self):
        markdown = "### they better fear hila"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        html = '<div><h3>they better fear hila</h3></div>'
        self.assertEqual(
           result,
           html
        )

    def test_markdown_to_html_node_paragraph(self):
        markdown = "happiness enfused with sorrow"
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        html = '<div><p>happiness enfused with sorrow</p></div>'
        self.assertEqual(
           result,
           html
        )

    def test_markdown_to_html_node_mixed(self):
        markdown = (
            "# This is a heading\n"
            "\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        )
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        html = '<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p></div>'
        self.assertEqual(
           result,
           html
        )

    def test_markdown_to_html_node_image(self):
        markdown = (
            "This is a paragraph of text. It has an image ![LOTR image artistmonkeys](/images/rivendell.png) inside of it."
        )
        node = markdown_to_html_node(markdown)
        result = node.to_html()
        html = '<div><p>This is a paragraph of text. It has an image <img src="/images/rivendell.png" alt="LOTR image artistmonkeys"></img> inside of it.</p></div>'
        self.assertEqual(
           result,
           html
        )

