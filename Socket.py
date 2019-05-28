import socket

# UDP 套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 对方的IP 以及端口
s.sendto(b"localhost", ('localhost', 80))

s.close()
