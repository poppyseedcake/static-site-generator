import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("test node", TextType.LINK, "http")
        node2 = TextNode("test node2", TextType.LINK, "http")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("test node", TextType.LINK, "https")
        node2 = TextNode("test node", TextType.LINK, "http")
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("test node", TextType.LINK)
        node2 = TextNode("test node", TextType.BOLD)
        self.assertNotEqual(node, node3)

if __name__ == "__main__":
    unittest.main()