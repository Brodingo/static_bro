import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('a', 'Boot.dev', None, {"href":"https://boot.dev","target":"_blank"})
        props = node.props_to_html()
        props_str = ' href="https://boot.dev" target="_blank"'
        self.assertEqual(props, props_str)

    def test_props_to_html2(self):
        node = HTMLNode('div', None, None, {"id":"content","class":"container"})
        props = node.props_to_html()
        props_str = ' id="content" class="container"'
        self.assertEqual(props, props_str)

    def test_props_to_html3(self):
        node = HTMLNode('iframe', None, None, {"src":"https://boot.dev","width":"640","height":"480"})
        props = node.props_to_html()
        props_str = ' src="https://boot.dev" width="640" height="480"'
        self.assertEqual(props, props_str)

    def test_values(self):
        node = HTMLNode('div', 'Hello world', None, {"id":"content"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello world")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"id":"content"})

    def test_repr(self):
        node = HTMLNode('div', 'Hello world', None, {"id":"content"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(div, Hello world, None, {'id': 'content'})"
        )

    def test_to_html(self):
        node = LeafNode('p', 'hi hungry im dad', {"class": "dadjoke"})
        self.assertEqual(
            node.to_html(),
            '<p class="dadjoke">hi hungry im dad</p>'
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, 'dya like baileys?')
        self.assertEqual(
            node.to_html(),
            "dya like baileys?"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )


if __name__ == "__main__":
    unittest.main()