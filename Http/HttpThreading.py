"""模仿服务器"""
import http
import re
import socket
import multiprocessing


def service_client(new_socket):
    """返回数据"""
    # 接收请求
    request = new_socket.recv(1024).decode("utf-8")
    print(request)
    request_list = request.splitlines()
    ret = re.match(r"[^/]+/(/[^ ]*)", request_list[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            pass
    # 返回浏览器的数据
    # 1.header
    # 2.body
    response = "HTTP?1.1 200 OK\r\n"
    response += "\r\n"
    # response += "<h1>哈哈哈</h1>"
    try:
        f = open("./html/index.html", "rb")
    except:
        response = "HTTP?1.1 404 OK\r\n"
        response += "\r\n"
        new_socket.setsockopt(response)
    else:
        response = "HTTP?1.1 404 OK\r\n"
        response += "\r\n"
        new_socket.setsockopt(response)

    html_content = f.read()
    f.close()
    # 将头发送
    new_socket.send(response.encode("utf-8"))
    # 将body发送
    new_socket.setsockopt(html_content)
    new_socket.close()


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 可以重复使用端口  而不阻塞 ⭐⭐⭐
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    # 绑定
    tcp_socket.bind(("", 8080))
    # 变为监听套接字
    tcp_socket.listen(128)
    # 接收连接
    while True:
        # 获取新的套接字
        new_socket, client_addr = tcp_socket.accept()
        # 为客户端服务
        p = multiprocessing.Process(target=service_client, args=(new_socket,))
        p.start()
        new_socket.close()
    # 关闭监听套接字
    tcp_socket.close()
