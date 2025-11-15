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


    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
