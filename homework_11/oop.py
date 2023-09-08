
class Main:
    mydict = dict()
    mytuple = tuple()

    def add_dict(self, key, item):
        if key not in self.mydict.keys():
            self.mydict[key] = item
            print("done", self.mydict)
        else:
            print("key already exist")

    def rem_dict(self, key):
        self.mydict.pop(key)
        print("Done", self.mydict)



    def add_tuple(self, item):
        new_list = list(self.mytuple)
        new_list.append(item)
        self.mytuple = tuple(new_list)
        print("done", self.mytuple)

    def count_tuple(self, item):
        new_value = self.mytuple.count(item)
        print("done", new_value)

    def index_tuple(self, item):
        new_index = self.mytuple.index(item)
        print("done", new_index)

    def getinfo(self):
        return self.mydict, self.mytuple

a = Main()


LoginAdmin = "Admin"
Password = "aaaa"

def menu():
    while True:
        print(" 1-Add dict \n 2-Add tuple \n 3-Get info \n 4-Delete item from dict \n 5-The number of repetitions of a certain value \n 6-Find the first index, for value: \n 10-Exit")
        answer = input("= ")
        if answer == "1":
            new_key = input("Type key:  ")
            new_item = input("Type value:  ")
            a.add_dict(new_key, new_item)
        elif answer == "2":
            new_value = input("Type value:  ")
            a.add_tuple(new_value)
        elif answer == "3":
            print(a.getinfo())
        elif answer == "4":
            for_delete = input("Type key:  ")
            a.rem_dict(for_delete)
        elif answer == "5":
            count = input("Type value:  ")
            a.count_tuple(count)
        elif answer == "6":
            index = input("Type index:  ")
            a.index_tuple(index)
        elif answer == "10":
            print("exit")
            break

def perm():
    while True:
        print("[1] Log in as an administrator\n[2] Log in as a user\n[0] Exit")
        user = input("= ")
        if user == "1":
            credlogin = input("Enter login =")
            credpass = input("Enter password =")
            if credlogin == LoginAdmin and credpass == Password:
                menu()
            else:
                print("Incorrect login or password")
        elif user == "2":
            print("done", a.getinfo())1

        elif user == "0":
            print("exit")
            break
perm()