from os import popen
from pydoc import text
from block_markdown import block_to_block_type, markdown_to_blocks
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)

    html_node = ParentNode(
        tag='div',
        children=[],
        props=None
    )

    for block in markdown_blocks:
        nodes = block_to_html_node(block)
        html_node.children.extend(nodes)

    return html_node

def block_to_html_node(markdown_block):
    block_type = block_to_block_type(markdown_block)
    html_nodes = []

    if block_type == "heading":
        heading_html_node = block_to_html_node_heading(markdown_block)
        html_nodes.append(heading_html_node)
    elif block_type == "code":
        code_html_node = block_to_html_node_code(markdown_block)
        html_nodes.append(code_html_node)
    elif block_type == "paragraph":
        para_html_node = block_to_html_node_para(markdown_block)
        html_nodes.append(para_html_node)
    elif block_type == "quote":
        quote_html_node = block_to_html_node_quote(markdown_block)
        html_nodes.append(quote_html_node)
    elif block_type == "unordered_list":
        ulist_html_node = block_to_html_node_unordered_list(markdown_block)
        html_nodes.append(ulist_html_node)
    elif block_type == "ordered_list":
        olist_html_node = block_to_html_node_ordered_list(markdown_block)
        html_nodes.append(olist_html_node)

    return html_nodes

def block_to_html_node_heading(markdown_block):
    heading_html_node = None
    heading_text = ''

    if markdown_block.startswith("######"):
        heading_html_node = ParentNode(tag='h6', children=[], props=None)
        heading_text = markdown_block[7:]
    elif markdown_block.startswith("#####"):
        heading_html_node = ParentNode(tag='h5', children=[], props=None)
        heading_text = markdown_block[6:]
    elif markdown_block.startswith("####"):
        heading_html_node = ParentNode(tag='h4', children=[], props=None)
        heading_text = markdown_block[5:]
    elif markdown_block.startswith("###"):
        heading_html_node = ParentNode(tag='h3', children=[], props=None)
        heading_text = markdown_block[4:]
    elif markdown_block.startswith("##"):
        heading_html_node = ParentNode(tag='h2', children=[], props=None)
        heading_text = markdown_block[3:]
    elif markdown_block.startswith("#"):
        heading_html_node = ParentNode(tag='h1', children=[], props=None)
        heading_text = markdown_block[2:]

    heading_text_node = text_to_textnodes(heading_text)
    heading_html_node_children = [text_node_to_html_node(node) for node in heading_text_node]
    heading_html_node.children.extend(heading_html_node_children)

    return heading_html_node


def block_to_html_node_code(markdown_block):
    code_text = markdown_block[3:-3]
    return LeafNode(tag='code', value=code_text, props=None)

def block_to_html_node_para(markdown_block):
    p_node = ParentNode(
        tag='p',
        children=[],
        props=None
    )
    text_nodes = text_to_textnodes(markdown_block)
    children_html_nodes = [text_node_to_html_node(node) for node in text_nodes]

    p_node.children.extend(children_html_nodes)

    return p_node


def block_to_html_node_quote(markdown_block):
    block_node = ParentNode(
        tag='blockquote',
        children=[],
        props=None
    )
    for line in markdown_block.split('\n'):
        if line == '':
            continue
        block_node.children.append(LeafNode(tag=None, value=line[2:], props=None))

    return block_node

def block_to_html_node_unordered_list(markdown_block):
    list_node = ParentNode(
        tag='ul',
        children=[],
        props=None
    )

    for line in markdown_block.split('\n'):
        list_item = ParentNode(tag='li', children=[], props=None)
        text_nodes = text_to_textnodes(line[2:])
        list_items = [text_node_to_html_node(node) for node in text_nodes]
        list_item.children.extend(list_items)
        list_node.children.append(list_item)

    return list_node

def block_to_html_node_ordered_list(markdown_block):
    list_node = ParentNode(
        tag='ol',
        children=[],
        props=None
    )

    for line in markdown_block.split('\n'):
        list_item = ParentNode(tag='li', children=[], props=None)
        text_nodes = text_to_textnodes(line.split(' ', 1)[1])
        list_items = [text_node_to_html_node(node) for node in text_nodes]
        list_item.children.extend(list_items)
        list_node.children.append(list_item)

    return list_node

