import multiprocessing


def main():
    q = multiprocessing.Queue()
    # 队列添加数据
    q.put("123")
    # 队列取数据
    q.get()
    # 判断队列是否为空
    q.empty()
