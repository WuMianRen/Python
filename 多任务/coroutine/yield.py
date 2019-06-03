# 方法中出现了yield 的时候方法会变成生成器
# 生成器是一种特殊的迭代器 也可以循环
# 按需加载
def create_nums():
    a = 1
    yield a
