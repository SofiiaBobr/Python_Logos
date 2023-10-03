print("First task")

inp = [1, 2, 45, 4, 5]


def gen(*args):
    aut = {}
    for i in range(0, len(args)):
        aut.update({args[i]: args[i] + 1})
        yield aut


a = gen(*inp)
for i in range(0, len(inp)):
    if i in range(0, len(inp)-1):
        next(a)
    else:
        print(next(a))

print("Second task")


def func(limit):
    for a in range(0, limit + 1):
        if a % 2 == 1:
            yield a


a = func(100)
for i in range(3):
    print(next(a))