import gevent

# 真实开发环境用 gevent
# 速度很快  协程运行时
# gevent 当中遇见延时的时候会自动切换
from gevent import monkey

# 进行程序补丁
monkey.patch_all()


# gevent 的自己的延时时间
gevent.sleep()
