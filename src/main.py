from textnode import TextNode, TextType, text_node_to_html_node

def main():
    node = TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev')
    print(node)
    leaf_node = text_node_to_html_node(node)
    print(leaf_node.to_html())


main()