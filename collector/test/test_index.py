import unittest

from index.local import ParserLocal
from index.market import ParserMarket
from index.world import ParserWorld


class TestIndexCollector(unittest.TestCase):

    def test_local(self):
        parser = ParserLocal()
        result = parser.parse()
        self.assertNotEqual(len(result), 0)

    def test_market(self):
        parser = ParserMarket()
        result = parser.parse()
        self.assertNotEqual(len(result), 0)

    def test_world(self):
        parser = ParserWorld()
        for currency in parser.currency:
            parser.parse(currency)
            self.assertNotEqual(len(parser.items), 0)


if __name__ == '__main__':
    unittest.main()
