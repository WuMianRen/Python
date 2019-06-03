"""
 实现可以迭代的对象
"""
from collections import Iterable


class ListMate(object):
    def __init__(self):
        self.names = list()
        self.nums = 0

    # 是一个可以迭代的对象的实例方法 ***
    # __iter__方法的返回值是一个迭代器
    def __iter__(self):
        return self

    def __next__(self):
        if self.nums < len(self.obj.names):
            ret = self.obj.names[self.nums]
            self.nums += 1
            return ret
        else:
            raise StopIteration

    def add(self, name):
        self.names.append(name)
