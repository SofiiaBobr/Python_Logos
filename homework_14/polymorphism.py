
class A:
    def __init__(self, a):
        self.a = a

    def getinfo(self):
        print(self.a)

    def sey_hello(self):
        print("Hello")

    def test(self):
        print('test')


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getinfo(self):
        print(self.a)
        print(self.b)

    def sey_hello(self):
        print("Hi")
class C:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getinfo(self):
        print(self.a)
        print(self.b)
        print(self.c)

    def new(self):
        print("bla")

class D:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.c = d

def search_metod(classs, list_metod):
    dict_class1 = []
    for i in range(len(list_metod)):
        dict_class1.append({})
    print(dict_class1)

    for a in classs:
        for j in range(len(list_metod)):
            if hasattr(a, list_metod[j]):
                dict_class1[j][a] = getattr(a, list_metod[j])
    return  dict_class1




classs = [A, B, C, D]

list_metod = []
for a in classs:
    for b in dir(a):

        if b[:2] != '__' and b not in list_metod:
            list_metod.append(b)


dict_class = search_metod(classs, list_metod)
for i in dict_class:
    for k,v in i.items():
        print(f'{k} - {v}')

