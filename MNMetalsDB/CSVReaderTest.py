import unittest
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        reader = CSVReader()
        reader.readFile('data/3351-RFQ-Tubes-and-accesories-V5.txt')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
