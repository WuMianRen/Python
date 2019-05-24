def main():
    list1 = [1, 3, 5, 7, 9, 100]
    list2 = ['hello'] * 5
    print(len(list1))  # 计算长度
    print(list1[0])  # 下标取数据
    # print(list1[5])  # IndexError: list index out of range 越界
    print(list[-1])  # 倒序取出
    list1[2] = 300  # 赋值
    # 添加元素
    list1.append(200)  # 追加元素
    list1.insert(1, 400)  # 指定索引加入
    list1 += [1000, 2000]
    print(list1)
    # 删除元素
    list1.remove(3)  # index remove
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)
    # 清空元素列表
    list1.clear()
    # 排序操作--内存拷贝
    list3 = sorted(list1)
    list4 = sorted(list1, reverse=True)  # 倒序
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list5 = sorted(list1, key=len)  # 长度排序
    list1.sort(reverse=True)  # 列表自身排序


main()


# 列表生成器生成List  ---阮一峰博客
import sys


def main():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


if __name__ == '__main__':
    main()
