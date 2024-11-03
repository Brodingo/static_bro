import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("this is another text node", TextType.TEXT)
        node2 = TextNode("this is another text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a bold text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("this is another text node", TextType.BOLD)
        node2 = TextNode("this is another text node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_text_to_leaf_node(self):
       text_node = TextNode("this is a text node", TextType.BOLD)
       leaf_node = text_node_to_html_node(text_node)
       self.assertEqual(
           leaf_node.to_html(),
           '<b>this is a text node</b>'
       )


if __name__ == "__main__":
    unittest.main()