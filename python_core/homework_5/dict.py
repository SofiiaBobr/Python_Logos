list1 = ("number1", "number2", "number3", "number4", "number5")
list2 = []
list4 = []
dicts = {}
dictss = {}


def validation(a):
    try:
        var = int(a)
        return True
    except ValueError:
        return False


def createListDictTwo(list):
    print("Create your list of values")
    f = 1
    while f in range(1, 6):
        print("Only integer numbers")
        print("order", f)
        inpu = input("Enter your number:  ")
        validresoult = validation(inpu)
        if validresoult is True:
            inp = int(inpu)
            list.append(inp)
            i = 0
        else:
            print("Wrong type")
            i = -1
        f = f + i + 1
    return list


def enterlist2(list):
    print("Do you want to create your own list of keys?")
    print("[1] Yes")
    print("[2] No")
    inpu = input("Make your choice:  ")
    validresoult = validation(inpu)
    if validresoult is True:
        inp = int(inpu)
        if inp == 1:
            list = createListDictTwo(list2)
        elif inp == 2:
            list.extend([1, 2, 3, 4, 5])
        else:
            print("There is no such option")
            enterlist2(list)
    else:
        print("Don't valid")
        enterlist2(list)
    return list


b = enterlist2(list2)


def createdict(a, c):
    print(c)
    print("First task")
    for i in range(len(a)):
        dicts[a[i]] = c[i]
    print(dicts)
    return dicts


createdict(list1, b)




def createDictTwo():
    print("Second task")
    listn = []
    listnn = []
    list1 = createListDictTwo(listn)
    print(list1)
    list2 = createListDictTwo(listnn)
    print(list2)
    for i in range(len(list1)):
        dictss[list1[i]] = list2
    print(dictss)


createDictTwo()