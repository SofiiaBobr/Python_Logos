class Data():
    LoginAdmin = "Admin"
    Password = "aaaa"

    mydict = dict()
    mytuple = tuple()

    def __init__(self):
        is_admin = self.perm()
        if is_admin != None:
            self.menu(admin = is_admin)
        else:
            pass

    def add_dict(self, key, item):
        if key not in self.mydict.keys():
            self.mydict[key] = item
            print("done")
        else:
            print("key already exist")

    def rem_dict(self, key):
        self.mydict.pop(key)
        print("Done")

    def add_tuple(self, item):
        new_list = list(self.mytuple)
        new_list.append(item)
        self.mytuple = tuple(new_list)
        print("done")

    def count_tuple(self, item):
        new_value = self.mytuple.count(item)
        print("done", new_value)

    def index_tuple(self, item):
        new_valeu = self.mytuple.index(item)
        print("done", new_valeu)

    def show_dict(self):
        print(self.mydict)


    def show_tuple(self):
        print(self.mytuple)


    def menu(self, admin=False):
        if admin:
            while True:
                print(
                    " 1-Add dict \n 2-Add tuple \n 3-Get info \n 4-Delete item from dict \n 5-The number of repetitions of a certain value in tuple \n 6-Find the first index, for value in tuple: \n 10-Go to back panel\n 11 - Exit-EXIT")
                answer = input("= ")
                if answer == "1":
                    new_key = input("Type key:  ")
                    new_item = input("Type value:  ")
                    self.add_dict(new_key, new_item)
                elif answer == "2":
                    new_value = input("Type value:  ")
                    self.add_tuple(new_value)
                elif answer == "3":
                    self.show_tuple()
                    self.show_dict()
                elif answer == "4":
                    for_delete = input("Type key:  ")
                    self.rem_dict(for_delete)
                elif answer == "5":
                    count = input("Type value:  ")
                    self.count_tuple(count)
                elif answer == "6":
                    index = input("Type value:  ")
                    self.index_tuple(index)
                elif answer == "10":
                    print("exit")
                    self.__init__()
                elif answer == "11":
                    print("exit")
                    exit()

        else:
            while True:
                answer = input('[1]  Show dict\n[2]  Show tuple\n[0] Go to back panel\n= ')
                if answer == '1':
                    self.show_dict()
                elif answer == '2':
                    self.show_tuple()
                elif answer == '0':
                    self.__init__()
                else:
                    print('401')


    def perm(self):
        while True:
            print("[1] Log in as an administrator\n[2] Log in as a user\n[0] Exit")
            user = input("= ")
            if user == "1":
                credlogin = input("Enter login =")
                credpass = input("Enter password =")
                if credlogin == self.LoginAdmin and credpass == self.Password:
                    return True
                else:
                    print("Incorrect login or password")
            elif user == "2":
                print("done you USER")
                return False

            elif user == "0":
                print("exit")
                return None
            else:
                print("Error, plz write now")


d = Data()