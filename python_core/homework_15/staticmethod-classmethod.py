class Main:
    x = 0

    @staticmethod
    def info(self, a, b, c):
        if not (self.isvalidate(a) and self.isvalidate(b) and self.isvalidate(c)):
            print("successfull")
        else:
            raise TypeError("Test")




    @classmethod
    def isvalidate(cls, x):
            if isinstance(x, int):
                cls.x = x
            elif x.isdigit():
                cls.x = x
            else:
                return True


a = Main()
print(a.info(a,'r', '4', 5))
print(a.x)