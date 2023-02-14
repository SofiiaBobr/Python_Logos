# I use number type int to make the task easier
lstint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Lsttext = ["a", "d", "c", "d", "e"]
suboption = str
def menu():
    print("[1] Add symbol")
    print("[2] Delete symbol")
    print("[0] Exit")


menu()

def submenu1():
    print("[1] Add number")
    print("[2] Add text")
    print("[0] Back")

def validation(a):
    try:
        var = int(a)
        return True
    except ValueError:
        return False

def delete_submenu():
    print("[1] You want delete number")
    print("[2] You want delete text")
    print("[0] Back")

def delete_sub_submenu_int():
    print("[1] delete specific number")
    print("[2] delete the number that is in order")
    print("[0] Back")

def delete_sub_submenu_text():
    print("[1] delete specific text")
    print("[2] delete the text that is in order")
    print("[0] Back")

option = int(input("Enter you options: "))
while option != 0:
    if option == 1:
        submenu1()
        suboption = int(input("Enter you options: "))
        while suboption != 0:
            if suboption == 1:
                print(lstint)
                symbol = input("Enter you number: ")
                index = input("Enter order where you want to see the number:  ")
                if validation(symbol) is True and validation(index) is True:
                        if int(symbol) not in lstint:
                            lstint.insert(int(index), int(symbol))
                            print(lstint)
                            print("Number added")
                            break
                        else:
                            print("This number is already in the list, choose another")
                elif validation(symbol) is False:
                    print("It is not a number")
                else:
                    print("Number in order where you want to see the text have invalid type")
            elif suboption == 2:
                print(Lsttext)
                symbol = input("Enter you text: ")
                index = input("Enter number in order where you want to see the text:  ")
                if validation(symbol) is False and validation(index) is True:
                    if symbol not in Lsttext:
                        Lsttext.insert(int(index), symbol)
                        print(Lsttext)
                        print("Text added")
                        break
                    else:
                        print("This symbol already in list ")
                elif validation(symbol) is True:
                    print("This is not a string")
                else:
                    print("Number in order where you want to see the text have invalid type")
            else:
                print("Bad choice")
                break

    elif option == 2:
        print("Delete")
        delete_submenu()
        delete_suboption=int(input("Enter you options: "))
        while delete_suboption != 0:
            if delete_suboption == 1:
                delete_sub_submenu_int()
                sub_sub_option = int(input("Enter you option:  "))
                while sub_sub_option != 0:
                    if sub_sub_option == 1:
                        print(lstint)
                        delete_number = input("Enter number what you want delete: ")
                        if validation(delete_number) is True:
                            if int(delete_number) in lstint:
                                lstint.remove(int(delete_number))
                                print("Number deleted")
                                print(lstint)
                                break
                            else:
                                print("This number not into list")
                                break
                        else:
                            print("This not a number")
                            break
                    elif sub_sub_option == 2:
                        print(lstint)
                        delete_index = input("Enter index number what you want delete: ")
                        if validation(delete_index) is True:
                            if int(delete_index) in lstint:
                                del lstint[int(delete_index)]
                                print("Number deleted")
                                print(lstint)
                                break
                            else:
                                print("Number with this index not into list")
                        else:
                            print("This not a number")
                            break
                    else:
                        print("Bad choice")
                        break
                print()
                delete_submenu()
                delete_suboption=int(input("Enter you options: "))

            elif delete_suboption == 2:
                delete_sub_submenu_text()
                sub_sub_option = int(input("Enter you options: "))
                while sub_sub_option != 0:
                    if sub_sub_option == 1:
                        print(Lsttext)
                        delete_text = input("Enter text what you want delete: ")
                        if validation(delete_text) is False:
                            if delete_text in Lsttext:
                                Lsttext.remove(delete_text)
                                print("Number deleted")
                                print(Lsttext)
                                break
                            else:
                                print("This text not into list")
                                break
                        else:
                            print("This not a text")
                            break
                    elif sub_sub_option == 2:
                        print(Lsttext)
                        delete_index = int(input("Enter index number what you want delete: "))
                        if validation(delete_index) is True:
                            if int(delete_index) <= len(Lsttext):
                                del Lsttext[int(delete_index)]
                                print("Text deleted")
                                print(Lsttext)
                                break
                            else:
                                print("Text with this index not into list")
                        else:
                            print("This not a index")
                            break
                    else:
                        print("Bad choice")
                        break
                print()
                delete_submenu()
                delete_suboption = int(input("Enter you options: "))


    print()
    menu()
    option = int(input("Enter you options: "))

print("Bye")
