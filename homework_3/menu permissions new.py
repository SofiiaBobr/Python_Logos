import random
import string
import math
import pprint

login = "a"
password = "1"
var = 0
letters = string.ascii_lowercase
a = ''.join(random.choice(letters) for i in range(81))
lststring = list(a)

integer_list = random.sample(range(10, 500), 15)
float_list = [x / 10 for x in integer_list]

Mainlist = lststring + float_list + integer_list

Newlist = Mainlist.copy()
def askcontin():
    option = input("\nDo you want to continue working with the menu?:  \n[1] Yes \n[0] No \nYour choice:  ")
    valid_option = validoption(option, 2)
    if valid_option is True:
        logic()
    elif valid_option is False:
        askcontin()
    elif int(option) == 0:
        print("\n---Bye----")


def prlist(Newlist):
    lents = math.ceil(((len(Newlist)) / 10))
    for i in range(1, lents + 1):
        print(Newlist[(i - 1) * 10:10 * i])


def validationInt(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


def validationfloat(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def validoption(op, n):
    validation_int = validationInt(op)
    if validation_int is True and int(op) in range(1, n):
        return True
    elif validation_int is False:
        print("The data type entered is incorrect, please try again")
        print()
        return False
        # valid(op, n)
    elif int(op) not in range(0, n):
        print("There is no such option, choose again")
        print()
        return False
        # valid(op, n)

def validnum(a):
    checkNum = validationfloat(a)
    if checkNum is True:
        b = list(a.split('.'))
        if len(b) > 1:
            return False
        else:
            return True
    else:
        print("It no number, try again")


def validstr(a):
    if validationfloat(a) is False:
        return True
    else:
        return False


def validlist(a):
    try:
        list(a)
        return True
    except ValueError:
        return False


def logasuser():
    print("Hi this is list")
    prlist(Newlist)
    askcontin()


def logasadm():
    cred = input("Enter your login and password:   \n")
    if len(cred.strip()) != 0:
        creds = cred.split()
        if creds[0] == login and creds[1] == password:
            prlist(Newlist)
            showadmpermish()
        else:
            print("Wrong credential, try egan")
            logasadm()
    else:
        print("Wrong credential, try egan")
        logasadm()


def addlist():
    print()
    symbol = input("Enter you list(use ',' like separator): ")
    check_list = validlist(symbol)
    symbolcool = symbol.split(',')
    if check_list is True:
        if symbolcool not in Newlist:
            Newlist.extend(list(symbolcool))
            print()
            prlist(Newlist)
            addmenu()
    else:
        print("Wrong something")
def addtext():
    print()
    symbol = input("Enter you text: ")
    index = input("Enter order where you want to see the text:  ")
    check_text = validstr(symbol)
    validation_int = validationInt(index)
    if check_text is True and validation_int is True:
        if symbol not in Newlist:
            Newlist.insert(int(index), symbol)
            prlist(Newlist)
            addmenu()
        else:
            print("This number is already in the list, choose another")
            addtext()
    elif validation_int is False:
        print("The data type index entered is incorrect, please try again")
        addtext()
    elif check_text is False:
        print("Invalid data type, text was expected, please try again")
        addtext()

def addnum():
    symbol = input("Enter you number: ")
    index = input("Enter order where you want to see the number:  ")
    check_num = validnum(symbol)
    validation_int = validationInt(index)
    if check_num is False and validation_int is True:
        if float(symbol) not in Newlist:
            Newlist.insert(int(index), float(symbol))
            prlist(Newlist)
            addmenu()
        else:
            print("This number is already in the list, choose another")
            addnum()
    elif check_num is True and validation_int is True:
        if int(symbol) not in Newlist:
            Newlist.insert(int(index), int(symbol))
            prlist(Newlist)
            addmenu()
        else:
            print("This number is already in the list, choose another")
            addnum()

    elif check_num is None:
        addnum()
    elif validation_int is False:
        print("The data type index entered is incorrect, please try again")
        addnum()

def addmenu():
    print("[1] Add number")
    print("[2] Add text")
    print("[3] Add list")
    print("[0] Back")
    print()
    option = input("Enter your option: ")
    valid_option = validoption(option, 4)
    if valid_option is True:
        opt = int(option)
        if opt == 1:
            addnum()
        elif opt == 2:
            addtext()
        elif opt == 3:
            addlist()
    elif valid_option is False:
        addmenu()
    else:
        showadmpermish()


def delind():
    index = input("Enter index symbol what you want delete: ")
    if validationInt(index) is True:
        ind = int(index)
        if ind <= len(Newlist):
            del Newlist[ind]
            prlist(Newlist)
            print("Symbol deleted")
            deletemenu()
        else:
            print("Symbol with this index doesn't exist")
            delind()
    else:
        print("Index wrong type, try again")
        delind()


def delsym():
    item_opt = input("Wryte symbol what you want to delete:  ")
    if item_opt in Newlist:
        Newlist.remove(item_opt)
        prlist(Newlist)
        print("Symbol deleted")
        deletemenu()
    else:
        print("This symbol is not in list")
        delsym()


def deletemenu():
    print("[1] delete specific item")
    print("[2] delete the item that is in order")
    print("[0] Back")
    option = input("Enter your option: ")
    validateOptionCustom = validoption(option, 3)
    if validateOptionCustom is True:
        opt = int(option)
        if opt == 1:
            delsym()
        elif opt == 2:
            delind()
    elif validateOptionCustom is False:
        deletemenu()
    elif int(option) == 0:
        showadmpermish()


def sort():
    print("[1] Sort by abc")
    print("[2] Sort by desc")
    print("[0] Back")
    option = input("Enter your option: ")
    validateOptionCustom = validoption(option, 3)
    if validateOptionCustom is True:
        opt = int(option)
        if opt == 1:
            Newlist1 = sorted([str(x) for x in Newlist])
            prlist(Newlist1)
            sort()
        elif opt == 2:
            Newlist1 = sorted([str(x) for x in Newlist], reverse=True)
            prlist(Newlist1)
            sort()
        elif int(option) == 0:
            showadmpermish()
    elif validateOptionCustom is False:
        sort()
    elif int(option) == 0:
        print()
        showadmpermish()

def seeid():
    print()
    print("This is the id the list:", id(Newlist))
    print()
    showadmpermish()

def validnum1(a):
    checkNum = validationfloat(a)
    if checkNum is True:
        b = list(a.split('.'))
        if len(b) > 1:
            return False
        else:
            return True
    else:
        print()

def check():
    option = input("Enter item what you want to check: ")
    validnumcustom = validnum1(option)
    if str(option) in Newlist:
        print("So this symbol is in the list")
    elif validnumcustom is True and int(option) in Newlist:
        print("So this symbol is in the list")
    elif validnumcustom is False and float(option) in Newlist:
        print("So this symbol is in the list")
    else:
        print("No, this symbol is not in the list")
    print()
    showadmpermish()


def showadmpermish():
    print("[1] Add to list")
    print("[2] Remove from list")
    print("[3] Sort list")
    print("[4] See id")
    print("[5] Check if item is in list")
    print("[0] Back")
    option = input("Enter your option: ")

    validateOptionCustom = validoption(option, 6)

    if validateOptionCustom is True:
        opt = int(option)
        # print(validoption(option, 5))
        if opt == 1:
            addmenu()
        elif opt == 2:
            deletemenu()
        elif opt == 3:
            sort()
        elif opt == 4:
            seeid()
        elif opt == 5:
            check()
    elif validateOptionCustom is False:
        showadmpermish()
    elif int(option) == 0:
        logic()


def logic():
    print("[1] Log in as an administrator")
    print("[2] Log in as a user")
    print("[0] Exit")
    option = input("Enter your option: ")
    valid_option = validoption(option, 3)
    if valid_option is True:
        opt = int(option)
        if opt == 1:
            logasadm()
        elif opt == 2:
            logasuser()
        else:
            print("\n---Bye----")
    elif valid_option is False:
        logic()
    else:
        print("\n---Bye----")


logic()



