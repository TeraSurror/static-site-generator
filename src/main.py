from textnode import TextNode, TextType

def main():
    tn = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")

    print(str(tn))

main()