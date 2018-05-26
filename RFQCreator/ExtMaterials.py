from Materials import Material

class ExtMaterials(Material):
    def __init__(self, material):
        self.orderNumber = "1"
        self.unit = "EA"
        self.quantity = 1.0
        self.setItemCode( material['itemcode'])
        self.setDescription(material['description'])
        self.setType(material['type'])
        self.setCategory(material['category'])
        self.setDimensions(material['dimensions'])

    def setOrderNumber(self,orderNum):
        self.orderNumber = orderNum

    def setUnit(self,unit):
        self.unit = unit

    def setQuantity(self,quantity):
        self.quantity = quantity

