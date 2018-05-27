class Quotes:
    def __init__(self):
        """clase basica de materiales cotizados"""
        self.internalCode = 0
        self.externalCode = 0
        self.providerCode = "X"
        self.receivedDate = "X"
        self.processedDate = "X"
        self.sentDate = "X"
        self.user = "X"
        self.providerName = "X"
        self.contactName = "X"
        self.incoterms = "X"
        self.materialList = []

    def setIntenalCode(self, code):
        self.internalCode = code

    def setExternalCode(self,code):
        self.externalCode = code

    def setProviderCode(self,code):
        self.providerCode = code

    def setUser(self,user):
        self.user = user

    def setProviderName(self,provider):
        self.providerName = provider

    def setContactName(self,contact):
        self.contactName = contact

    def setMaterialList(self, materials):
        for mt in materials:
            self.materialList.append(mt)

    def setReceivedDate(self,date):
        self.receivedDate = date

    def setProcessedDate(self,date):
        self.processedDate = date

    def setInconterms(self,incoterm):
        self.incoterms = incoterm

    def to_json(self):
        obj_list = [ ob.__dict__ for ob in self.materialList]
        return obj_list
