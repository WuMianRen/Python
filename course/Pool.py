import multiprocessing


def work():
    pass


def main():
    # 创建进程池
    # 只允许三个进程运行
    po = multiprocessing.Pool(3)
    po.apply_async(work, (1,))
    # 一定要用 关闭进程池 然后执行close
    po.join()
    po.close()
