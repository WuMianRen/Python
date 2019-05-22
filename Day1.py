# *表示可变参数 [C#:params]
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))


# 没有函数的重载 会执行后面的函数体
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


foo()  # goodbye, world!


class Module:
    def foo(self):
        pass

    def bar(self):
        pass

    # __name__是Python中一个隐含的变量它代表了模块的名字
    # 只有被Python解释器直接执行的模块的名字才是__main__
    if __name__ == '__main__':
        print('call foo()')
        foo()
        print('call bar()')
        bar()


class ActionScope:
    def foo(self):
        b = 'hello'
         
        def bar():  # Python中可以在函数内部再定义函数
            c = True
            print(a)
            print(b)
            print(c)

        bar()
        # print(c)  # NameError: name 'c' is not defined

    if __name__ == '__main__':
        a = 100
        # print(b)  # NameError: name 'b' is not defined
        foo()
