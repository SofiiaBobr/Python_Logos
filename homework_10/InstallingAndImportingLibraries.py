import random
import string

def createRandomInput():
    import random
    import string
    random = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(1000000)])
    with open('text.txt', 'w') as txt:
        txt.write(random)


createRandomInput()


def seemsLikeSort():
    dct = {}
    with open('text.txt', 'r') as txt:
        lst = txt.read().replace('\n', '')
        print(lst)
        freq = 0
        for char in lst:
            char.isalpha()
            if char.isalpha() == True:
                freq = freq + 1
                if char.isalpha() == True and char.isalpha and char not in dct.keys():
                    dct[char] = 1
                elif char.isalpha() == True and char.isalpha and char in dct.keys():
                    dct[char] += 1
        print(freq)
        print(dct.items())


seemsLikeSort()