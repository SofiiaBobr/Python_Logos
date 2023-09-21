class House():

    def __init__(self):
        self.Prise = 0
        self.High = 1
        self.Area = 0
        print("House", self)



class Villa(House):
    def __init__(self):
        super().__init__()
        self.pool = 1
        self.High = 3
        print("Villa", self)
    def info(self):
        print(self.Area, self.High, self.Prise, self.pool)

class Coteg(House):
    def __init__(self):
        super().__init__()
        self.terassa = 2
        self.Area = 100
    def info(self):
        print(self.Area, self.High, self.Prise, self.terassa)

myCoteg = Coteg()
myVilla = Villa()
myCoteg.info()
myVilla.info()