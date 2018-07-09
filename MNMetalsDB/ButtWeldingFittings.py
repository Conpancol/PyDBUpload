class ButtWeldingFitting:
    def __init__(self):
        """BUTT WELDING FITTINGS ACCORDING TO ANSI/ASME SANDVIK"""
        self.fittingType = "BUTT WELDING FITTING"
        self.category = ""
        self.standards = ""
        self.pipeSize = "X"
        self.schedule = "X"
        self.dimensions = "X"
        self.weight = 0.0

    def setCategory(self, cat):
        self.category = cat

    def setStandars(self,standards):
        self.standards = standards

    def setPipeSize(self, size):
        self.pipeSize = size

    def setSchedule(self, sch):
        self.schedule = sch

    def setDimensions(self, dims):
        self.dimensions = dims

    def setWeight(self, weight):
        self.weight = weight

