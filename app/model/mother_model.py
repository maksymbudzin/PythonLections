from abc import ABC, abstractmethod


class AbstractParrant(ABC):

    def hello_my_kids(self):
        raise NotImplementedError

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Mother(AbstractParrant):

    def __init__(self, age):
        self.age = age
        print("Mother constructor")

    def do_work(self):
        print("i`m working")

    def do_house_work(self):
        print("listening music")


class Father(AbstractParrant):

    def __init__(self):
        print("Father constructor")

    def play_guitar(self):
        print("father is plaing guitar")

    def do_house_work(self):
        print("sitting in the sofa and drinking beer")


class Daughter(Mother, Father):

    def hello_my_kids(self):
        print("hello daughter")

    def hello_friend(self):
        print("hello")

    def __init__(self, age=0):
        Father.__init__(self)
        Mother.__init__(self, age=age)

    def do_work(self):
        print("i`m working like a horse")


class Friend:
    pass


def greet_mother(mother: Mother):
    print("Hello mother")
    mother.do_work()


def greet_father(father: Father):
    print("papa")
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daughter()
    daughter.hello_friend()
    daughter.hello_my_kids()
    daughter.do_house_work()
    # change parrents
    for x in [daughter]:
        x.do_house_work()

    # list
    povtorochka = ["mathan_2", "programming_2"]

    # tuple
    vasian = ("11 years", 22, 3.14, daughter)

    # set
    my_set = {23, 11, 10, 10, "call"}
    print(my_set)

    # frozen_set
    anouther_set = frozenset(["he", "ll", "ow"])

    # dictionary
    my_dict = {1: "first", "1": 12, (1, 2, 3): "dict"}