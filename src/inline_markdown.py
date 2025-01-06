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

