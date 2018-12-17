import csv
import re
import datetime
import copy
import pdb
import unittest


def transfo_text():
    with open('sales1.csv') as f:
        data = f.read()

    lines = data.split('\n')
    data_list = []
    for line in lines:
        print(line)
        data_list.append(line.split(','))

    print(data_list)


def transfo_csv():
    with open('sales1.csv') as f:
        data = list(csv.reader(f))
        print(data)


def errors():
    try:
        with open('bob') as f:
            print('bob')
    except FileNotFoundError as err:
        print(err)


class ClassExample: #(motherClass)
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def class_print(self):
        print(self.param1 + self.param2)


def list_comprehension():
    L = [1,2,3,4,5]
    M = [x for x in L if x % 2 == 0]
    print(M)


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
    list_string[1] ='am'
    print(list_string)
    string = ''.join(list_string)
    print(string)
    print(string.upper())


def copy_shallow_deep():
    L = [[1,2],[3,4]]
    M = L
    N = L.copy()
    O = L[:]
    P = copy.deepcopy(L)
    L.append(0)
    L[0] = 0
    L[1][0] = 'a'
    print("After append\nM = {}\nN = {}\nO = {}\nP = {}".format(M,N,O,P))


def sort():
    L = [-3, 5, 2]
    M = sorted(L)
    print("After sorted(L)\nL = {}\nM={}".format(L, M))
    L.sort(reverse=True)
    print("After L.sort(reversed = True)\nL = {}\nM={}".format(L, M))
    L.sort(key = lambda x : x * x)
    M = sorted(L, key=lambda x : x * x)
    print("After L.sort(key square) and M=sorted(L, key)\nL = {}\nM={}".format(L, M))


g_var = 2


def global_ex():
    g_var = g_var
    return g_var


def is_equal_in():
    A = 3
    B = 3.0
    print("A = {} and B = {}\nA == B is {}\nA is B is {}".format(A, B, A == B, A is B))
    L = [B, B]
    print("A in [B, B] is {}".format(A in L))


def book_tuple_list():
    print("(3) is a {} and (3,) is a {})".format(type((3)), type((3,))))
    L = [i for i in range(9)]
    print("L = {}\n L[1:6:2] = {}".format(L, L[1:6:2]))


def book_string():
    A = 'bob'
    A += " l'éponge"
    print(A)
    print(type(A))
    print(u'\U0001F600 trop styish')
    values = {
        'name': 'bob',
        'age': '25'
    }
    print('{name} is {age} year old'.format(**values))

def book_dict():
    D = {'a': 'b', 'c': 'd'}
    print(D.get('a',-1), D.get('f', -1), D.get('f'))
    D.setdefault('cc', 33)
    print(D)


def book_bitwise():
    a = 23
    b = 37
    print(a, b)
    c = a << 1 & b
    d = a << 1 | b >> 1
    print(c, d)


def book_assignment():
    a, b, c = 1, (2,), (3,4)
    L = (a, b),c
    print(L)
    a, b = b, a
    print(a, b)

import sys
def book_import():
    print(sys.path)
    sys.path.insert(0, '~/PycharmProjects')
    print(sys.path)

def book_iterable():
    r1 = range(3)
    r2 = range(1, 10, 3)
    print("range(3) = {}".format(r1))
    for i in r1:
        print(i)
    print("range(1,10,3) = {}".format(r2))
    for i in r2:
        print(i)


def book_exception():
    try:
        a = 4 / 0
        print(a)
    except:
        print("error")
    try:
        string = None
        if string == None:
            raise Exception('string shouldn\'t be empty')
    except Exception as e:
        print(e)


def book_function_params(normal_arg, default_val_arg='blue', *args, **kwargs):
    print('normal_arg = {}'.format(normal_arg))
    print('default_val_arg = {}'.format(default_val_arg))
    print('arg_list (*args) = {}'.format(args))
    print('arg_keywords (**kwargs) = {}'.format(kwargs))


def book_function():
    book_function_params('green',0, 'bob1', 'bob2', clef='clef1', clef2='clef2')
    book_function_params('green')
    book_function_params('green', clef='clef1', clef2='clef2')


def book_generator():
    yield 'aaa'
    yield 'aaa'
    yield 'b'
    yield 'c'
    yield 'aaa'


def book_iteration():
    iterator = book_generator()
    for a in iterator:
        print(a)


class BadInitClass:
    def __init__(self, items=[]):
        self.items = items

    def print_items(self):
        self.items += [3]
        print("BadInitClass items = {}".format(self.items))

class GoodInitClass:
    def __init__(self, items = None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def print_items(self):
        self.items += [3]
        print("BadInitClass items = {}".format(self.items))


def compare_classes():
    a = BadInitClass()
    b = BadInitClass()
    a.print_items()
    b.print_items()
    a = GoodInitClass()
    b = GoodInitClass()
    a.print_items()
    b.print_items()

class StaticClassInstance:
    static_data = 'bob'

    def __init__(self):
        self.instance_data = 'hoho'
        # if not self not accessible outside function __init__

    def print_self(self):
        print("self.instance_data = {}".format(self.instance_data))
        self.instance_data += " instance"
        print("added ' instance' to instance_data\nself.instance_data = {}".format(self.instance_data))
        #print(static_data) doesn't work
        print("self.static_data = {}".format(self.static_data))
        self.static_data += " instance"
        print("added 'static_data' to static data\nself.static_data = {}".format(self.static_data))

    @classmethod
    def print_class(cls):
        cls.static_data += " class"
        print("cls.static_data = {}".format(cls.static_data))

    @staticmethod
    def print_nl():
        print('\ncreation of other instance\n')


def static_class_instance():
    a = StaticClassInstance()
    a.print_self()
    a.print_class()
    a.print_self()
    a.print_nl()
    b = StaticClassInstance()
    b.print_self()
    b.print_class()
    b.print_self()


# transfo_text()
# transfo_csv()
# print(dir())
# errors()
# ClassExample(2, 3).class_print()
# regex()
# dates()
# strings()
# copy_shallow_deep()
# sort()
# global_ex()
# is_equal_in()

# book_tuple_list()
# book_string()
# book_dict() # how to access dict with no error or set value if doesn't exist
# book_bitwise()
# book_assignment()
# book_import()
# book_iterable()
# book_exception()
# book_function()
# book_iteration()
# compare_classes()
# static_class_instance()
# pdb.run('compare_classes()')
help(unittest)






"""
Comment ca marche import module --> si besoin pip install
Pourquoi on utilise is et pourquoi on utilise == , exemple de None
Expliquer variable reference, objet valeur et q auoi sert del
Quels sont les 4 numeric type 
File open: what are the modes and why. what needs to be done once file open
How to get information on file (get current position, set curent position relatively or absolutely
PRopertues of set
What happens when we do assignement
How to make a module both importable and runable why does it work?
Where does import look for modules? how to add directories
What is an iterable
What is try/except/raise statement
What is a context manager
Fonction: a quoi sert def, default return ? comment fonctionnes les parametres + a quoi faire attention avec default arg
What is a decorator
What is the system iterator, generator, yield
What is a package?
What is a class, what to pay attention with constructor and what are different variable methods and decorators
What is an interface
What is a private member
How to run pdb?
How to run unit tests
"""
