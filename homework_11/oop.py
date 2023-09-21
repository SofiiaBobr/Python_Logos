
class Main:
    mydict = dict(name = "John", age = 36, country = "Norway")
    mytuple = tuple([1, 2, 3])

    def add_dict(self, key, item, admin = False):
        if admin:
            if key not in self.mydict.keys():
                self.mydict[key] = item
                print("done", self.mydict)
            else:
                print("key already exist")
        else:
            print("403")

    def rem_dict(self, key, admin = False):
        if admin:
            self.mydict.pop(key)
            print("Done", self.mydict)
        else:
            print("403")


    def add_tuple(self, item, admin = False):
        if admin:
            new_list = list(self.mytuple)
            new_list.append(item)
            self.mytuple = tuple(new_list)
            print("done", self.mytuple)
        else:
            print("403")
    def count_tuple(self, item, admin = False):
        if admin:
            new_value = self.mytuple.count(item)
            print("done", new_value)
        else:
            print("403")
    def index_tuple(self, item, admin = False):
        if admin:
            new_index = self.mytuple.index(item)
            print("done", new_index)
        else:
            print("403")

    def getinfo(self):
        return self.mydict, self.mytuple

a = Main()


LoginAdmin = "Admin"
Password = "aaaa"
isadmin = False

def menu():
    while True:
        print(" 1-Add dict \n 2-Add tuple \n 3-Get info \n 4-Delete item from dict \n 5-The number of repetitions of a certain value \n 6-Find the first index, for value: \n 10-Exit")
        answer = input("= ")
        if answer == "1":
            new_key = input("Type key:  ")
            new_item = input("Type value:  ")
            a.add_dict(new_key, new_item, isadmin)
        elif answer == "2":
            new_value = input("Type value:  ")
            a.add_tuple(new_value, isadmin)
        elif answer == "3":
            print(a.getinfo())
        elif answer == "4":
            for_delete = input("Type key:  ")
            a.rem_dict(for_delete, isadmin)
        elif answer == "5":
            count = input("Type value:  ")
            a.count_tuple(count, isadmin)
        elif answer == "6":
            index = input("Type index:  ")
            a.index_tuple(index, isadmin)
        elif answer == "10":
            print("exit")
            break

def perm():
    global isadmin
    while True:
        print("[1] Log in as an administrator\n[2] Log in as a user\n[0] Exit")
        user = input("= ")
        if user == "1":
            credlogin = input("Enter login =")
            credpass = input("Enter password =")
            if credlogin == LoginAdmin and credpass == Password:
                isadmin=True
                break
            else:
                print("Incorrect login or password")
        elif user == "2":
            print("done", a.getinfo())

        elif user == "0":
            print("exit")
            break
perm()
menu()