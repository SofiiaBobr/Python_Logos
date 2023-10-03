#import json
import items as items

dct = {'number1': 1, 'number2': 2, 'number3': 3, 'number4': 4, 'number5': 5}


def add(**kwargs):
    print("Task one")
    print(type(kwargs))
    text = open("test.txt", "w")
    text.write(f"{str(kwargs)}\n")
    text.close()
    text = open("test.txt", "r")
    print(text.read())
    text.close()


add(**dct)


def nen():
    print("Task two")
    text = open("test.txt", "r")
    a = eval(text.read())
    text.close()
    print(type(a))
    return a


c = nen()


def gen(**c):
    for key in c:
        yield key, c[key]


for pair in gen(**c):
    print(pair)





