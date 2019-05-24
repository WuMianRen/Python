"""
    1.元组中的元素是无法修改的
    2.可以在多线程且数据不重复的时候使用
    3.一个方法返回多个值时 可以使用
    4.元组在创建时间和占用的空间上面都优于列表
    5.Python中的集合跟数学上的集合是一致的，
    不允许有重复元素，而且可以进行交集、并集、差集等运算。


"""

def main():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)


main()