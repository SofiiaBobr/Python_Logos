class Main:
    def __str__(self):
        return f'key: {self.key}, value:{self.value}'

    def __init__(self, key, value):
        self.key = key
        self.value = value

class Dictionary:
    def __init__(self, input_dict):
        self.input_dict = self.create_list(input_dict)

    @classmethod
    def create_list(cls, input_dict):
        mylist = []
        for i, j in input_dict.items():
            if isinstance(i, str):
                mylist.append(Main(i, j))
        return mylist
a = {('hello', 43): ['a', 1],
     'python': ['b', 2],
     'a': ['str', 5]
     }

x = Dictionary(a)

for i in x.input_dict:
    print(i)