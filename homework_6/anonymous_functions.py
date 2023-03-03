listRandom = [1, '2', 3, '5', 2, '8', 7, '6', 4, '0', 8, '09', 78, 6]
print("Original list\n", listRandom)

print("\nPart 1")
transform = map(lambda x: str(x) if isinstance(x, int) else int(x), listRandom)
print(list(transform))


print("\nPart 2")


def transfor(x):
    if isinstance(x, int):
        return str(x)
    elif isinstance(x, str):
        return int(x)


transformap = map(transfor, listRandom)
print(list(transformap))


print("\nPart 3")


def tuple():
    inp = input("Create list, use tab tu split:  ")
    list = inp.split(' ')
    d = *list,

    print(d[0:10])
    print(type(d))

tuple()