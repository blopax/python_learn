import csv
import re
import datetime
import copy


# Questions:
# Comment chopper la date d'aujourd'hui sous la forme ("on est le 3 juin. Il est 4h45")
# Comment transformer la phrase "bob aime la semoule" en "boby aime la semoule"
# Prevoir ce que print les fonctions ci-dessous


def regex():
    string1 = 'Where are you going'
    print(re.findall('.e', string1))
    print(re.sub('.e.', 'bob', string1))

    tel = '06-45-32-76-89'
    print(re.findall(r"(^(06)((-[0-9]{2}){4}))", tel))
    print(re.search(r"(^(06)((-[0-9]{2}){4}))", tel))


def dates():
    date = datetime.datetime.utcnow()
    print(date)
    print(date.day)
    print(date.strftime("%D hour %M"))


def strings():
    string = 'bob aime la semoule'
    list_string = list(string)
    list_string[1] = 'am'
    print(list_string)
    string = ''.join(list_string)
    print(string)
    print(string.upper())


def copy_shallow_deep():
    L = [[1, 2], [3, 4]]
    M = L
    N = L.copy()
    O = L[:]
    P = copy.deepcopy(L)
    L.append(0)
    L[0] = 0
    L[1][0] = 'a'
    print("After append\nM = {}\nN = {}\nO = {}\nP = {}".format(M, N, O, P))


def sort():
    L = [-3, 5, 2]
    M = sorted(L)
    print("After sorted(L)\nL = {}\nM={}".format(L, M))
    L.sort(reverse=True)
    print("After L.sort(reversed = True)\nL = {}\nM={}".format(L, M))
    L.sort(key=lambda x: x * x)
    M = sorted(L, key=lambda x: x * x)
    print("After L.sort(key square) and M=sorted(L, key)\nL = {}\nM={}".format(L, M))


g_var = 2


def global_ex():
    l_var = g_var
    g_var = l_var
    print(l_var)
    print(g_var)
    return g_var


def is_equal_in():
    A = 3
    B = 3.0
    print("A = {} and B = {}\nA == B is {}\nA is B is {}".format(A, B, A == B, A is B))
    L = [B, B]
    print("A in [B, B] is {}".format(A in L))



print(dir())
regex()
# dates()
# strings()
copy_shallow_deep()
sort()
global_ex()
is_equal_in()



# Autres fonctions de bases

def transfo_text():
    with open('sales1.csv') as f:
        data = f.read()
        for line in f:
            print(line)

    lines = data.split('\n')
    data_list = []
    for line in lines:
        data_list.append(line.split(','))
    print(data_list)


def transfo_csv():
    with open('sales1.csv') as f:
        data = list(csv.reader(f))
        print(data)


def errors():
    try:
        with open('bob'):
            print('bob')
    except FileNotFoundError as err:
        print(err)


class ClassExample:  # (motherClass)
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def class_print(self):
        print(self.param1 + self.param2)


def list_comprehension():
    L = [1, 2, 3, 4, 5]
    M = [x for x in L if x % 2 == 0]
    print(M)
