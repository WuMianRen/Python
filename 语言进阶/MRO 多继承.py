"""
    super() 只会调用父类的一次方法：可以匹配执行顺序根据MRO
        xxx.__mro__ 这样可以获得调用的先后顺序【C3 算法】
"""


class Person(object):
    # 类属性
    name = "我的"

    # 类方法
    @classmethod
    def class_func(cls):
        """
            至少有一个cls参数、
            cls 里面是类对象的引用
         """
        pass

    @staticmethod
    def static_func():
        """ 默认无参数 直接调用 """
        pass

    # 实例属性
    def __init__(self, age):
        """
            默认self参数
            self 里面是实例对象的引用
         """
        self.age = age

    @property
    # property属性内部进行一系列的逻辑运算并且返回值
    def property_func(self):
        """只可以有一个self参数"""
        pass

    # 读写器 [比较C# get;set;]
    @property_func.setter
    def property_func(self, value):
        """赋值的方式会调用这个方法"""
        pass

    @property_func.deleter
    def property_func(self):
        """del 可以调用这个方法"""
        pass

    AGE = property()


person = Person("wode")
person.__class__.name = ""  # 这样的方式可以修改类属性
ret = person.property_func  # 可以直接掉用property_func 并且将返回值直接返回，调用方法变成了调用属性

""" with 关键字 [比较C# using ]"""
# 此关键字会释放上下文[context]
# __exit__ __enter__ 当有这两个方法的对象就实现了上下文管理器
# __enter__ 返回值返回到定义的值(f)  [as f]
# 实现上下文管理器

from contextlib import contextmanager  # 上下文管理库


@contextmanager
def my_open(path, mode):
    pass
