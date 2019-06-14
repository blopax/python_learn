import csv
import re
import datetime
import copy
import pdb
import unittest



# Predict next functions


def book_tuple_list():
    print("(3) is a {} and (3,) is a {})".format(type((3)), type((3,))))
    L = [i for i in range(9)]
    print("L = {}\n L[1:7:2] = {}".format(L, L[1:7:2]))


def book_string():
    A = 'bob'
    A += " l'éponge"
    print(A)
    print(type(A))
    u = u'\U0001F600'
    print(u + " trop stylish")
    print(type(u))
    values = {
        'name': 'bob',
        'age': '25'
    }
    print('{name} is {age} year old'.format(**values))


def book_dict():
    D = {'a': 'b', 'c': 'd'}
    print(D.get('a', -1), D.get('f', -1), D.get('f'))
    D.setdefault('cc', 33)
    D.setdefault('c', 33)
    print(D)


def book_bitwise():
    a = 23
    b = 37
    print(bin(a), bin(b))
    print(int(a << 1), int(b >> 1))
    c = a << 1 & b
    d = a << 1 | b >> 1
    print(c, d)


def book_assignment():
    a, b, c = 1, (2,), (3, 4)
    L = (a, b), c
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
    book_function_params('green', 0, 'bob1', 'bob2', clef='clef1', clef2='clef2')
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
    print(book_generator)
    print(book_generator())


class BadInitClass:
    def __init__(self, items=[]):
        self.items = items

    def print_items(self):
        self.items += [3]
        print("BadInitClass items = {}".format(self.items))


class GoodInitClass:
    def __init__(self, items=None):
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
        # print(static_data) doesn't work
        print("self.static_data = {}".format(self.static_data))
        self.static_data += " static_data"
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


book_tuple_list()
book_string()
book_dict() # how to access dict with no error or set value if doesn't exist
book_bitwise()
book_assignment()
book_import()
book_iterable()
book_exception()
book_function()
book_iteration()
compare_classes()

static_class_instance()


# help(unittest)
# pdb.run('compare_classes()')


