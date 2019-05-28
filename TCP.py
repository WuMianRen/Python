import socket


def main():
    # 创建TCP
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = ""
    server_port = ""

    tcp_client_socket.connect(server_ip, server_port)
    send_data = ""

    tcp_client_socket.send(send_data)

    tcp_client_socket.close()


def main2():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.bind("", 7890)
    tcp_client_socket.listen(128)
    client_data, client_addr = tcp_client_socket.accept()
    print(client_data)
    print(client_addr)
    recv_data = client_data.recv(1027)
    print(recv_data)
