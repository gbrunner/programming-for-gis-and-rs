class Parcel:
    def __init__(self, landuse, value):
        self.landuse = landuse
        self.value = value
    def assessment(self):
        if self.landuse == "SFR":
            rate = 0.05
        elif self.landuse == "MFR":
            rate = 0.04
        else:
            rate = 0.02
        assessment = self.value * rate
        return assessment 
