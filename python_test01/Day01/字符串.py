"""
字符串的定义
"""
def string_create():
    # 定义字符串
    str1 = "hello world"
    str2 = 'hello world'
    str3 = """hello world"""
    str4 = '''hello world'''

    # 获取字符串长度
    print(len(str1))

    # 字符串拼接
    str5 = str1 + str2
    print(str5)

    # 字符串重复
    str6 = str1 * 3
    print(str6)

    # 字符串索引
    print(str1[0])

    # 字符串切片
    print(str1[0:2])

    # 转义
    print('hello\nworld')
    print('hello\\world')
    print(r'hello\nworld') # r开头代表原始字符串，不会转义
    # 进制
    print('\141\142\143\x61\x62\x63')
    print('\u9a86\u660a')
    # 比较
    print('abc' == 'abc')
    # 存在
    print('a' in 'abc')
    # 去除空格
    print('  hello world  '.strip())
    print('%hello world  '.lstrip('%'))
    print('  hello world  '.rstrip())
    # 替换
    print('hello world'.replace('world', 'python'))
    print('hello world'.replace('world', 'python',2)) # 增加替换的次数


def string_upper():
    str1 = 'hello world'
    print(str1.upper())
    print(str1.lower())
    print(str1.capitalize())
    print(str1.title())

def string_find():
    str1 = 'hello world'
    print(str1.find('o'))
    print(str1.find('s')) # -1 find 找不到会返回-1
    print(str1.rfind('o'))
    print(str1.index('o'))
    print(str1.rindex('o'))
    print(str1.index('s')) # ValueError: substring not found

def string_type():
    str1 = 'hello world'
    print(str1.startswith('h'))
    print(str1.endswith('d'))
    print(str1.isdigit()) # False 是否是纯数字
    print(str1.isalpha()) # False 是否是纯字母（空格不算）
    print(str1.isalnum()) # False 是否是字母数字混合

def string_split():
    """
    拆分 split
    合并 join
    :return:
    """
    str1 = 'hello world 222'
    print(str1.split(' '))
    print(str1.split(' ', 1)) #最大拆分粒度，所以有分左右
    print(str1.rsplit(' ', 1))
    print(str1.splitlines())
    #第一部分是分隔符之前的内容。
    #第二部分是分隔符本身。
    #第三部分是分隔符之后的内容。
    print(str1.partition(' ')) #('hello', ' ', 'world 222')
    print(str1.rpartition(' ')) #('hello world', ' ', '222')
    print(str1.strip())
    print(str1.lstrip())
    print(str1.rstrip())
    print(str1.replace('o', 'O'))

def string_join():
    str1 = 'hello world'
    print(' '.join(str1))
    print(''.join(str1))
    print(''.join(str1.split(' ')))
    print(''.join(str1.split(' ')).strip())
    print(''.join(str1.split(' ')).lstrip())
    print(''.join(str1.split(' ')).rstrip())

def string_format():
    str1 = 'hello world'
    print('%s' % str1)
    print(str1.center(20,'*'))
    print(str1.ljust(20,'*'))
    print(str1.rjust(20,'*'))
    print("33".zfill(5))# 左侧补零 00033
    print("-33".zfill(5)) # 左侧补零 -0033
    a,b = 321, 123
    print("{0} {1}".format(a,b))
    print("{1} {0}".format(a,b))
    print("{0:>10} {1:<10}".format(a,b)) # 右侧补空格
    print("{0:^10} {1:^10}".format(a,b)) # 居中
    print('%d * %d = %d' % (a,b,a*b))
    print('{0} * {1} = {2}'.format(a,b,a*b))
    print(f'{a} * {b} = {a*b}')

def string_encode_decode():
    """
    在 Python 中，b 前缀表示字节对象（bytes），而不是普通的字符串对象（str）。
    UTF-8 编码是一种可变长度的字符编码方式，能够高效地表示 Unicode 字符集中的字符。
    :return:
    """
    str = '中文'
    b = str.encode('utf-8') #b'\xe4\xb8\xad\xe6\x96\x87'  字节表示
    print(b)
    print(b.decode('utf-8'))

if __name__ == '__main__':
    string_encode_decode()