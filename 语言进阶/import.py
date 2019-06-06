"""
    import xxx

    from xxx import  xxx

    import xxx as yyy  起别名



"""

import sys

sys.path  # 寻找当前模块搜索的位置

# 将模块放入
sys.path.append()
sys.path.insert(0, "")
from imp import reload

reload(sys)  # 重新导入
