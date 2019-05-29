import socket
import threading


# 接收数据
def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


# 发送数据
def send_msg(udp_socket, dest_ip, dest_prot):
    while True:
        send_data = input("")
        udp_socket.send(send_data.encode("utf-8"), (dest_ip, dest_prot))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp_socket.bind(("", 7890))
    dest_ip = input("获取对方的ip")
    dest_port = int(input("获取对方的端口"))

    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_port, dest_ip))
    t_recv.start()
    t_send.start()
