from datetime import datetime
import time



class Main:
    Z = None
    def __init__(self, x, y, z = Z):
        self._x = x
        self.__y = y
        self.z = z

    def __write_info(self):
        file = open('data.txt', 'a')
        time = datetime.now()
        file.write(f" {time.strftime('%d/%m/%Y, %H:%M:%S')}\n x = {self._x}; y = {self.__y}; z = {self.z}\n")
        file.close()

    def set_x(self, x):
        self._x = x
        print("Successful")
        self.__write_info()

    def set_y(self, y):
        self.__y = y
        print("Successful")
        self.__write_info()

    def set_z(self, z):
        self.z = z
        print("Successful")
        self.__write_info()
        
        

a = Main(5,6, 8)
time.sleep(3)
a.set_x(1)
time.sleep(1)
a.set_y(2)
time.sleep(1)
a.set_z(3)



