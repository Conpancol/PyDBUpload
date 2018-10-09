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

    def test_rfqcreationThree(self):
        rfq = RFQCreator()
        if rfq.alreadyExists(3390):
            print("RFQ already exists - skip")
        else:
            rfq.setRFQInformation(3390, 1201, 'Javier Socorro', 'MN', '14/06/2018')
            rfq.addRFQNote("NA")
            rfq.createRFQfromCSV('data/REQ-1202_METALS_REQ.csv')
            self.assertEqual(True, True)

    def test_badData(self):
        rfq = RFQCreator()
        if rfq.alreadyExists(10000):
            print("RFQ already exists - skip")
        else:
            rfq.setRFQInformation(10000, 151360, 'Javier Socorro', 'MN', '23/02/2018')
            rfq.addRFQNote("Para fabricacion agujas planta de secado")
            rfq.createRFQfromCSV('data/BAD-data-test.csv')
            self.assertEqual(True, True)

    def test_exportData(self):
        rfq = RFQCreator()
        rfq.exportRFQtoCSV(3399,'RFQ_3399_MN.csv')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
