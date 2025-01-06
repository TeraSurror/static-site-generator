from htmlnode import HTMLNode
from inline_markdown import extract_markdown_images, split_nodes_image
from textnode import TextNode, TextType

def main():
    node = TextNode( 
        "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.NORMAL_TEXT,
    )

    got = split_nodes_image([node])

    for g in got:
        print(g)

main()