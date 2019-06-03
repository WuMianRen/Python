"""
    多任务文件夹拷贝
"""
import os
import multiprocessing


def main():
    # 获取拷贝的文件夹
    old_folder_name = input()
    # 创建新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 获取文件夹中所有带XXX 的文件的名字 listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)
    # 创建进程池
    po = multiprocessing.Pool(5)
    # 创建一个队列
    # 当前的队列是进程池之间的队列
    q = multiprocessing.Manager().Queue()

    for file_name in file_names:
        po.apply_async(copy, args=(q, file_name, old_folder_name, new_folder_name))
    po.close()
    while True:
        file_name = q.put()


# 复制文件夹


def copy(q, file_name, old_folder_name, new_folder_name):
    # 读取数据
    print("模拟拷贝文件" + file_name)
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    # 写入数据
    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()
    q.get(file_name)
