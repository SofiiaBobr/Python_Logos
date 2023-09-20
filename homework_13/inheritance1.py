class Animal():
    def __init__(self, size, number_of_paws, tail, whiskers, color):
        self.size = size
        self.number_of_paws = number_of_paws
        self.tail = tail
        self.whiskers = whiskers
        self.color = color
        print("Animal", self)
        print("\n")

    def update(self, size, number_of_paws, tail, whiskers, color):
        self.size = size
        self.number_of_paws = number_of_paws
        self.tail = tail
        self.whiskers = whiskers
        self.color = color
        print("Update susseccfull")

class Dog(Animal):
    def __init__(self, size, number_of_paws, tail, whiskers, color, breed):
        super().__init__(size, number_of_paws, tail, whiskers, color)
        print("Dog", self)
        self.breed = breed


    def Characteristics(self):
        print("Dog")
        print("size", self.size)
        print("number_of_paws", self.number_of_paws)
        print("tail", self.tail)
        print("whiskers", self.whiskers)
        print("breed", self.breed)
        print("color", self.color, "\n")

class Hamster(Animal):
    def __init__(self, size, number_of_paws, tail, whiskers, color, fingers):
        self.d = {}
        super().__init__(size, number_of_paws, tail, whiskers, color)
        self.size = size
        self.tail = tail
        self.fingers = fingers


        print("Hamster", self)

    def dictionary(self, *args):
        key_set = set()
        value_set = set()
        for pair in args:
            if isinstance(pair, tuple) and len(pair) == 2:
                key, value = pair
                key_set.add(key)
                if isinstance(value, (int, float, str, bool)):
                    value_set.add(value)
                else:
                    print(f"Value {value} is not a valid type and will be skipped.")
        print(key_set, value_set)

    def Characteristics(self):
        print("Hamster")
        print("fingers", self.fingers)
        print("size", self.size)
        print("number_of_paws", self.number_of_paws)
        print("tail",self.tail)
        print("whiskers", self.whiskers)
        print("color", self.color, "\n")


myDog = Dog("Big", 4, True, True, "brown", "haski")
myDog.Characteristics()
myHamster = Hamster("Small", 4, False, True, "white", True)
myHamster.Characteristics()
myDog.update("midle", 4, True, True, "black")
myHamster.update("Small", 4, False, True, "grey")
myDog.Characteristics()
myHamster.Characteristics()
myHamster.dictionary(("key1", 42), ("key2", "value2"), ("key3", 3.14), ("key4", [1, 2, 3]))