from textnode import TextNode, TextType

def main():
    node = TextNode("Some text", TextType.LINK, "http://google.com")
    print(repr(node))



if __name__ == "__main__":
    main()
