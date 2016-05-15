import unittest

from src.parse.parse import Parse


class ParseTests(unittest.TestCase):

    def test_check_if_parse_initializes_with_query(self):
        parse = Parse("This is a test")
        self.assertEqual(parse.query, "This is a test")
