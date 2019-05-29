import threading
import time


class TestGlobal:
    g_num = 100
    nums = [11, 22]

    # 在一个函数中   全局变量修改时看对全局变量的指向改变的使用global

    def test(self):
        global g_num
        g_num += 1
        print(g_num)

    def test2(self):
        print(g_num)

    def main(self):
        # target 指定调用那个函数
        # args表示传递所用的参数是那个
        t1 = threading.Thread(target=self.test, args=self.g_num)
        t2 = threading.Thread(target=self.test2)
        t1.start()
        time.sleep(1)
        t2.start()
        time.sleep(1)

# 线程安全
