import random
from functools import reduce

print(list(filter(lambda x: x - 2 == 4, [1, 2, 3, 4, 5, 6])))

print(reduce(lambda x, y: x + x, [1, 2, 3, 4]))

na = "你好"
print(bytes(na, encoding="gbk").decode("gbk"))

dict()


class A(object):

    def __init__(self):
        self.__name = "hhh"


def pp(self, i):
    self.i = i


A.pp = pp
a = A()

a.pp(100)

b = ["1", "2", "3"]
print(enumerate(b))
for i, m in enumerate(b):
    print(i)
    print(m)
