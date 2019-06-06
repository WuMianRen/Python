"""
    __private  私有属性
    _protected  受保护的  禁止导入
    __XX__      魔法属性一般不使用
    XX_         避免关键字冲突
"""


class Test:
    # 只能对当前的类有效   对其子类无效
    # 限定Test对象只能绑定_name, _age和_gender属性
    __slots__ = "foo", "too"

    def __init__(self, foo, too):
        # 属性变为了私有[__]
        self.__foo = foo
        # 属性为受保护[_]
        self._too = too

    # 方法变为了私有
    def __bar(self):
        print(self._foo)

    # 公共的方法
    def call(self):
        pass


def main():
    test = Test("Hello", "World")
    print(test._Test__foo)  # 这样可以访问到私有属性
