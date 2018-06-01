import unittest
from RFQCreator import RFQCreator

class RFQTestCase(unittest.TestCase):
    def test_rfqcreation(self):
        rfq = RFQCreator()
        if rfq.alreadyExists(3388):
            print("RFQ already exists - skip")
        else:
            rfq.setRFQInformation(3388, 111001, 'Javier Socorro', 'MN', '25/04/2018')
            rfq.addRFQNote("Project 111001")
            rfq.createRFQfromCSV('data/3388.csv')
            self.assertEqual(True, True)

    def test_rfqcreationTwo(self):
        rfq = RFQCreator()
        if rfq.alreadyExists(3364):
            print("RFQ already exists - skip")
        else:
            rfq.setRFQInformation(3364, 151360, 'Javier Socorro', 'MN', '23/02/2018')
            rfq.addRFQNote("Para fabricacion agujas planta de secado")
            rfq.createRFQfromCSV('data/3364.csv')
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
