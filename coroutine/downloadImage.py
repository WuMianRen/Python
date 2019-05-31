import urllib.request
import gevent


# 获取网页的内容
def download(image_name, image_url):
    req = urllib.request.urlopen(image_url)
    image_content = req.read()
    with open(image_name, "wb") as f:
        f.write(image_content)

# 利用协程进行多任务
def main():
    gevent.joinall([
        gevent.spawn(download, "1.jpg", "网址"),
        gevent.spawn(download, "2.jpg", "网址")
    ])
