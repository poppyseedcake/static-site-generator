import unittest
from generate import extract_title


class TestGenerte(unittest.TestCase):
    def test_extracttitle(self):
        md = """
# This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
"""
        blocks = extract_title(md)
        self.assertEqual(
            blocks,
            "This is **bolded** paragraph",
        )

    def test_extracttitle_no_header(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
"""
        self.assertRaises(
            Exception,
            extract_title,
            md,
        )