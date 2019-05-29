import threading
import time

# 线程运行是没有顺序的
def say_sorry():
    for i in range(5):
        print("hahah")
        time.sleep(1)


def thread_start():
    t1 = threading.Thread(target=say_sorry)
    t1.start()

    # 获取运行的线程
    print(threading.enumerate())




