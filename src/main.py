from htmlnode import HTMLNode
from textnode import TextNode, TextType

def main():
    tn = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    h1_html_node = HTMLNode("h1", "This is some text", None, None)
    div_html_node = HTMLNode("div", None, [h1_html_node], {'style': "text-align:center"})

    print(str(tn))
    print(div_html_node)

main()