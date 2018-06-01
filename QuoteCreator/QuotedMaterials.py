from ExtMaterials import ExtMaterials

class QuotedMaterials(ExtMaterials):
    def __init__(self,material):
        """clase basica de materiales metalicos con cotizacion"""
        self.theoreticalWeight = 0.00
        self.givenWeight = 0.00
        self.unitPrice = 0.00
        self.totalPrice = 0.00
        self.note = "NA"
        self.setItemCode(material['itemcode'])
        self.setDescription(material['description'])
        self.setType(material['type'])
        self.setCategory(material['category'])
        self.setDimensions(material['dimensions'])

    def setTheoreticalWeight(self, theoWeight):
        self.theoreticalWeight = theoWeight

    def setGivenWeight(self,givenWeight):
        self.givenWeight = givenWeight

    def setUnitPrice(self,unitPrice):
        self.unitPrice = unitPrice

    def setTotalPrice(self,total):
        self.totalPrice = total

    def setNote(self,note):
        self.note = note



