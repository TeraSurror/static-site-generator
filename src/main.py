from htmlnode import HTMLNode
from inline_markdown import extract_markdown_images
from textnode import TextNode, TextType

def main():
    tn = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    h1_html_node = HTMLNode("h1", "This is some text", None, None)
    div_html_node = HTMLNode("div", None, [h1_html_node], {'style': "text-align:center"})

    print(str(tn))
    print(div_html_node)


    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    got = extract_markdown_images(text)
    for a, b in got:
        print(a, b)

main()