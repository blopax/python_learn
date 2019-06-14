class Person:
    surname = "Thomas"
    name = "Pablo"

    def __init__(self):
        self.name = "Gautier"

    def hello(cls):
        print(f"{cls.surname}")
        print(f"{cls.name}")

    @classmethod
    def hello_2(cls):
        print(f"{cls.surname}")
        print(f"{cls.name}")

    @classmethod
    def change_surname(cls):
        cls.surname = "gvann"


if __name__ == "__main__":
    Gautier = Person()
    Thomas = Person()

    print("======= test 1 ======")
    Gautier.hello()
    Thomas.hello()
    print('\n')

    Gautier.surname = "gvann"
    print("======= test 2 ======")
    Gautier.hello()
    Thomas.hello()
    print('\n')

    print("======= test 3 ======")
    Gautier.hello_2()
    Thomas.hello_2()
    print('\n')

    del Gautier
    Gautier = Person()
    Gautier.change_surname()

    print("======= test 4 ======")
    Gautier.hello()
    Thomas.hello()
    print('\n')

    print("======= test 5 ======")
    Gautier.hello_2()
    Thomas.hello_2()
    print('\n')
