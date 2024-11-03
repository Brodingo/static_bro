from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value or delimiter not in node.text:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        split_nodes = node.text.split(delimiter)
        sub_nodes = []
        for i in range(len(split_nodes)):
            if split_nodes[i] == "":
                continue
            if i % 2 == 0:
                sub_nodes.append(TextNode(split_nodes[i],TextType.TEXT))
            else:
                sub_nodes.append(TextNode(split_nodes[i],text_type))
        new_nodes.extend(sub_nodes)
    return new_nodes
