from ExtMaterials import ExtMaterials

class QuotedMaterials(ExtMaterials):
    def __init__(self,material):
        """clase basica de materiales metalicos con cotizacion"""
        self.theoreticalWeight = 0.00
        self.givenWeight = 0.00
        self.unitPrice = 0.00
        self.totalPrice = 0.00

    def setTheoreticalWeight(self, theoWeight):
        self.theoreticalWeight = theoWeight

    def setGivenWeight(self,givenWeight):
        self.givenWeight = givenWeight

    def setUnitPrice(self,unitPrice):
        self.totalPrice = unitPrice

    def setTotalPrice(self,total):
        self.totalPrice = total


