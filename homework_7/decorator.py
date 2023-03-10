dictss = {}
inputx = []


def validationInt(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


def createCorrectList(input3):
    for i in range(0, len(input3)):
        if validationInt(input3[i]) is True:
            inputx.append(int(input3[i]))
        else:
            inputx.append(str(input3[i]))
    return inputx


def createFirstDict(input4, c):
    r = listArg(input4)
    h = *r,
    dictx = {}
    for i in range(len(input4)):
        dictss.update({h[i]: {input4[i]: c[i]}})
    return dictss


def listArg(d):
    h = []
    for i in range(0, len(d)):
        h.append(str(i)+" arg")
    return h



def type_and_value_decorator(func):
    def wrapper():
        print("without any repetitions")
        input1 = input("Enter you list by one line with tab separator: ")
        input2 = input1.split(" ")
        input3 = list(input2)
        input4 = createCorrectList(input3)
        c = list(map(lambda x: "int" if isinstance(x, int) else "str", input4))
        dicts = createFirstDict(input4, c)
        func(dicts)
    return wrapper


@type_and_value_decorator
def func(*args):
    print("Hello")
    print(*args)


func()

#type_and_value_decorator(func)()
