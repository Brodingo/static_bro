import os

from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def format_quote(block):
    lines = block.split('\n')
    text = []
    for line in lines:
        text.append(line.lstrip(">").strip())
    children = text_to_children('\n'.join(text))
    return ParentNode('blockquote', children)

def format_unordered_list(block):
    children = []
    lines = block.split('\n')
    for line in lines:
        children.append(ParentNode('li', text_to_children(line[2:])))
    return ParentNode('ul', children)

def format_ordered_list(block):
    children = []
    lines = block.split('\n')
    for line in lines:
        children.append(ParentNode('li', text_to_children(line[3:])))
    return ParentNode('ol', children)

def format_code(block):
    children = text_to_children(block[3:-3])
    return ParentNode('pre', [
        ParentNode('code', children)
    ])

def format_heading(block):
    split = block.split(' ',1)
    h_size = len(split[0])
    return ParentNode(f"h{h_size}", text_to_children(split[1]))

def format_paragraph(block):
    return ParentNode('p', text_to_children(block))

def block_to_html_node(block, block_type):
    match block_type:
        case 'quote':
            node = format_quote(block)
        case 'unordered_list':
            node = format_unordered_list(block)
        case 'ordered_list':
            node = format_ordered_list(block)
        case 'code':
            node = format_code(block)
        case 'heading':
            node = format_heading(block)
        case 'paragraph':
            node = format_paragraph(block)
        case _:
            raise Exception("unsupported block type")
    return node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(block_to_html_node(block, block_type))
    return ParentNode('div', children, None)

