import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
        else:
            split_nodes = []
            sections_arr = old_node.text.split(delimiter)
            if len(sections_arr) % 2 == 0:
                raise ValueError('Invalid markdown: formatted section nor closed')

            for i in range(len(sections_arr)):
                if sections_arr[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(text=sections_arr[i], text_type=TextType.NORMAL_TEXT))
                else:
                    split_nodes.append(TextNode(text=sections_arr[i], text_type=text_type))
            new_nodes.extend(split_nodes)
        
    return new_nodes
    
def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        split_nodes = []
        for image_alt, image_src in images:
            text_sections = text.split(f'![{image_alt}]({image_src})', 1)
            split_nodes.append(TextNode(text=text_sections[0], text_type=TextType.NORMAL_TEXT))
            split_nodes.append(TextNode(text=image_alt, text_type=TextType.IMAGE_TEXT, url=image_src))
            text = ''.join(text_sections[1:])
        
        if text:
            split_nodes.append(TextNode(text=text, text_type=TextType.NORMAL_TEXT))
        new_nodes.extend(split_nodes)

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        split_nodes = []
        for alt, href in links:
            text_sections = text.split(f'[{alt}]({href})', 1)
            split_nodes.append(TextNode(text=text_sections[0], text_type=TextType.NORMAL_TEXT))
            split_nodes.append(TextNode(text=alt, text_type=TextType.LINK_TEXT, url=href))
            text = ''.join(text_sections[1:])
        
        if text:
            split_nodes.append(TextNode(text=text, text_type=TextType.NORMAL_TEXT))
        new_nodes.extend(split_nodes)

    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.NORMAL_TEXT)
    nodes = [text_node]

    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    for node in nodes:
        print(node)

    return nodes

