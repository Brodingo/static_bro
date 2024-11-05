import re

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

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT.value or not images:
            new_nodes.append(node)
            continue
        original_text = node.text
        for image in images:
            image_alt = image[0]
            image_url = image[1]
            split_nodes = original_text.split(f"![{image_alt}]({image_url})", 1)
            if split_nodes[0] != '':
                new_nodes.append(TextNode(split_nodes[0],TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            original_text = split_nodes[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT.value or not links:
            new_nodes.append(node)
            continue
        original_text = node.text
        for link in links:
            link_title = link[0]
            link_url = link[1]
            split_nodes = original_text.split(f"[{link_title}]({link_url})", 1)
            if split_nodes[0] != '':
                new_nodes.append(TextNode(split_nodes[0],TextType.TEXT))
            new_nodes.append(TextNode(link_title, TextType.LINK, link_url))
            original_text = split_nodes[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes