import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()