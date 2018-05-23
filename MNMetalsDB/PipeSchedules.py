class PipeSchedule:
    def __init__(self):
        """Tabla de wall thickness segun schedule"""
        self.schedule = "X"
        self.nps = "1"
        self.od = 0.0
        self.wt = 0.0
        self.npsMM = 0.0
        self.odMM = 0.0
        self.wtMM = 0.0
        self.code = ""

    def setSchedule(self,code):
        self.schedule = code

    def setNps(self,nps):
        self.nps = nps

    def setOd(self,od):
        self.od = od

    def setWt(self,wt):
        self.wt = float(wt)

    def setNpsMM(self,nps):
        self.npsMM = float(nps)

    def setOdMM(self,od):
        self.odMM = float(od)

    def setWtMM(self,wt):
        self.wtMM = float(wt)

    def setCode(self,code):
        self.code = "SCH" + code

    # Getters

    def getSchedule(self):
        return self.schedule

    def getNps(self):
        return self.nps

    def getOd(self):
        return self.od

    def getWt(self):
        return self.wt

    def getNpsMM(self):
        return self.npsMM

    def getOdMM(self):
        return self.odMM

    def getWtMM(self):
        return self.wtMM

    def getCode(self):
        return self.code

    def __str__(self):
        return self.getCode() + ' ' \
               + self.getSchedule() + ' ' \
               + str(self.getNps()) + ' ' \
               + str(self.getWt()) + ' '  \
               + str(self.getNpsMM()) + ' ' \
               + str(self.getWtMM())
