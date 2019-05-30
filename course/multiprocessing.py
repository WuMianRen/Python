import multiprocessing


def test():
    pass


def test2():
    pass


# 多进程创建的多任务
def main():
    p1 = multiprocessing.Process(target=test)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()
