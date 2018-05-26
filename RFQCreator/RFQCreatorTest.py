import unittest
from RFQCreator import RFQCreator

class RFQTestCase(unittest.TestCase):
    def test_rfqcreation(self):
        rfq = RFQCreator()
        rfq.setRFQInformation(3388, 111001, 'Javier Socorro', 'MN', '25/04/2018')
        rfq.createRFQfromCSV('data/3388.csv')
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
