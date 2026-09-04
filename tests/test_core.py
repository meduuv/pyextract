import unittest

from pyextract import first_present, get_path


class ExtractTests(unittest.TestCase):
    def test_nested_mapping(self):
        self.assertEqual(get_path({"user": {"name": "medu"}}, "user.name"), "medu")

    def test_sequence_index(self):
        self.assertEqual(get_path({"items": ["a", "b"]}, "items.1"), "b")

    def test_default(self):
        self.assertEqual(get_path({}, "missing.value", "fallback"), "fallback")

    def test_first_present(self):
        self.assertEqual(first_present({"b": 2}, ["a", "b"]), 2)


if __name__ == "__main__":
    unittest.main()
