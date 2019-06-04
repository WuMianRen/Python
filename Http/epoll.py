"""
    epoll: 内存映射，事件通知
"""

import socket
import select


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(False)  # 支持非堵塞
epl = select.epoll()

epl.poll()
