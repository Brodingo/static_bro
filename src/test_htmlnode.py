import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()