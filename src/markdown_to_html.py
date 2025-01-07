from block_markdown import block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode
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
    
    return html_nodes

def block_to_html_node_heading(markdown_block):
    heading_html_node = None
    heading_text = ''

    if markdown_block.startswith("#"):
        heading_html_node = ParentNode(tag='h1', children=[], props=None)
        heading_text = markdown_block[2:]
    elif markdown_block.startswith("##"):
        heading_html_node = ParentNode(tag='h2', children=[], props=None)
        heading_text = markdown_block[3:]
    elif markdown_block.startswith("###"):
        heading_html_node = ParentNode(tag='h3', children=[], props=None)
        heading_text = markdown_block[4:]
    elif markdown_block.startswith("####"):
        heading_html_node = ParentNode(tag='h4', children=[], props=None)
        heading_text = markdown_block[5:]
    elif markdown_block.startswith("#####"):
        heading_html_node = ParentNode(tag='h5', children=[], props=None)
        heading_text = markdown_block[6:]
    elif markdown_block.startswith("######"):
        heading_html_node = ParentNode(tag='h6', children=[], props=None)
        heading_text = markdown_block[7:]

    heading_text_node = text_to_textnodes(heading_text)
    heading_html_node_children = [text_node_to_html_node(node) for node in heading_text_node]
    heading_html_node.children.extend(heading_html_node_children)

    return heading_html_node


