import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode(tag="p",value="text test",)
        str = "tag: p\ntext test"
        self.assertEqual(node, str)

if __name__ == "__main__":
    unittest.main()