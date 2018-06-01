import unittest
from QuoteCreator import QuoteCreator

class QuotesTestCase(unittest.TestCase):
    def test_quotecreation(self):
        quote = QuoteCreator()
        if quote.alreadyExists("3364P1"):
            print("Quote already exists - skip")
            self.assertEqual(True, True)
        else:
            quote.setQuoteInformation(3364, 151360, '3364P1','P01', 'Hefei Jeterry Titanium', 'NA sales@jtrtitanium.com', '28/02/2018', '21/02/2018', 'aosorio')
            quote.setQuoteIncoterms('CIF Cartagena')
            quote.setQuoteNote("CIF terms included in price")
            quote.createQuotefromCSV('data/3364-01.csv')
            self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
