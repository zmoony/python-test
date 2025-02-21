"""
变量
运算符
"""

def variable():
    """
    惯例1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
    惯例2：受保护的变量用单个下划线开头。
    惯例3：私有的变量用两个下划线开头。

    转换
    int()：将一个数值或字符串转换成整数，可以指定进制。
    float()：将一个字符串（在可能的情况下）转换成浮点数。
    str()：将指定的对象转换成字符串形式，可以指定编码方式。
    chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
    ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。

    :return:
    """
    # 整形
    print(1111)
    #二进制
    print(0b100)
    #八进制
    print(0o100)
    #十六进制
    print(0x100)

    #浮点形
    print(1.1)
    print(1.23456e2)

    #字符串
    print('hello world')
    print("hello world")
    print('''hello world''')
    print("""hello world""")
    print('''
    hello world
    ''')
    print("""
    hello world
    """)
    print('hello\nworld')
    print('hello\tworld')
    print('hello\bworld')

    #Bool
    print(True)
    print(False)

    # 判断类型
    print(type(True))

    #转换
    print(int('123'))
    print(int('123',base=16))
    print(int('100',base=2))
    print(float('1.1'))

def operator():
    """
    运算符
    算术 + - * / //（整除） % （取模） **（幂）
    赋值运算符和复合赋值运算符 = += *= :=
    比较运算符 ==、!=、<、>、<=、>=
    逻辑运算符 and、or和 not
    :return:
    """
    print(5 // 2)
    print(5 % 2)
    a = 1
    a += 2
    print((a:=8))  # 有返回值 海象运算符
    # print((a=8))  会报错

def convert_fahrenheit_to_celsius():
    """
    将华氏温度转换为摄氏温度 C=(F−32)/1.8
    """
    fahrenheit = float(input('请输入华氏温度：'))
    celsius = (fahrenheit - 32) / 1.8
    # f 代表需要格式化
    print(f'{fahrenheit:.1f}华氏温度转换为摄氏温度为{celsius:.1f}摄氏度')
    print('%.1f华氏温度转换为摄氏温度为%.1f摄氏度' % (fahrenheit,celsius))

if __name__ == '__main__':
    convert_fahrenheit_to_celsius()