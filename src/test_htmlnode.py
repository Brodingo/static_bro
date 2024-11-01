import unittest

from htmlnode import HTMLNode, LeafNode


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


if __name__ == "__main__":
    unittest.main()