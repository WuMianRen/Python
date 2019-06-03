"""
 实现可以迭代的对象
"""
from collections import Iterable


class ListMate(object):
    def __init__(self):
        self.names = list()

    # 是一个可以迭代的对象的实例方法 ***
    # __iter__方法的返回值是一个迭代器
    def __iter__(self):
        return ListIterator(self)

    def add(self, names):
        self.names.append(names)


# 这个方法就是迭代器
class ListIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.nums = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.nums < len(self.obj.names):
            ret = self.obj.names[self.nums]
            self.nums += 1
            return ret
        else:
            raise StopIteration


listMate = ListMate()
# 判断是否是迭代器
classmate_iterator = iter(listMate)
next(classmate_iterator)

for name in listMate:
    print(name)
