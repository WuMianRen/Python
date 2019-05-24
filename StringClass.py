def main():
    str1 = 'hello,world!'
    # 获取长度
    print(len(str1))  # 13
    print(str1.capitalize())  # Hello,world!
    print(str1.upper())  # HELLO,WORLD!
    print(str1.find('or'))  # 8
    print(str1.find('sdasdas'))  # -1 表示未找到
    # 这两个找不到会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    print(str1.startswith('hel'))  # True 是否是规定的开头
    print(str1.endswith('!'))  # True 是否是规定的结尾
    print(str1.center(50, '*'))  # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.rjust(50, ' '))  # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    str2 = 'abc123456'
    print(str2[2])  # c
    print(str2[2:5])  # c12
    print(str2[2:])  # c-end
    print(str2[2::2])  # c246 隔一位取
    print(str2[::2])  # ac246
    print(str2[::-1])  # 倒序读出
    print(str2[-3:-1])  # 45
    print(str2.isdigit())  # False 检查是否是数字构成
    print(str2.isalpha())  # False 检查是否是字母组成
    print(str2.isalnum())  # True 检查是否是字母和数字组成
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


main()
