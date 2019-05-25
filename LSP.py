"""
里氏替换原则--通过继承来实现
在父类出现的地方可以透明的使用子类来代替
"""
from abc import abstractmethod, ABCMeta


class Person(object, metaclass=ABCMeta):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

    # 可以被覆写的方法  实现多态的方式
    @abstractmethod
    def overWrite(self):
        pass


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

    def overWrite(self):
        pass


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

    # 子类覆写父类的方法
    def overWrite(self):
        pass


def main():
    stu = Student("周四", 15, '初三')
    stu.study('数学')
    stu.watch_av()  # 同时调用了父类的watch_av 方法
    t = Teacher('骆昊', 38, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()
