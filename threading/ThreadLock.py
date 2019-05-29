import threading


# 加锁原则：尽量少的代码块加锁

def main():
    # 互斥锁
    mutex = threading.Lock()
    # 开启锁
    mutex.acquire()
    # 释放锁
    mutex.release()


