""""
函数和模块
* 之后必须是强制关键字
/ 之前的顺序不可更改
"""
import functools
import random
import string
import time
from functools import reduce, wraps


def func_test(a=3, *args, **kwargs):
    """
    有默认值的，默认值放在最后
    :param a: 参数，默认值
    :param args:可变参数
    :param kwargs:可变关键字参数
    :return:
    """
    print(a)
    print(args)
    print(kwargs)

def generate_code(*,code_len = 4):
    """
    随机验证码
    string.digits '0123456789'
    string.ascii_letters 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random模块的sample和choices函数都可以实现随机抽样，
    sample实现无放回抽样，这意味着抽样取出的元素是不重复的；
    choices实现有放回抽样，这意味着可能会重复选中某些元素。
    这两个函数的第一个参数代表抽样的总体，而参数k代表样本容量，需要说明的是choices函数的参数k是一个命名关键字参数，在传参时必须指定参数名。
    :return:
    """
    ALL_CHARS = string.digits + string.ascii_letters
    return "".join(random.choices(ALL_CHARS, k=code_len))

def is_prime(num: int) -> bool:
    """
    判断一个数是否为素数
    int 强制参数类型
    bool 说明返回值类型
    :param num:
    :return:
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def calc(init_values, op_func, *args, **kwargs):
    """
    使用函数作为参数
    :param init_values: 初始值
    :param op_func: 计算方法
    :param args: 参数
    :param kwargs: 关键词参数
    :return:
    """
    items = list(args)+list(kwargs.values())
    result = init_values
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def calc_add(a, b):
    """
    加法
    :param a:
    :param b:
    :return:
    """
    return a + b
def calc_sub(a, b):
    """
    减法
    :param a:
    :param b:
    :return:
    """
    return a - b

# 高级函数-filter map
def fun_filter_map():
    old_nums = [35, 12, 8, 99, 60, 52]
    # 第一种写法
    new_nums = list(map(lambda x: x * 2,filter(lambda x: x > 20, old_nums)))
    # 第二种写法
    new_nums2 = [x * 2 for x in old_nums if x > 20]
    print(new_nums)
    print(new_nums2)

# 高级函数-sorted (函数无副作用，有返回值，不会修改原有的函数)
def fun_sorted():
    old_nums = [35, 12, 8, 99, 60, 52]
    # 奇数在前，偶数在后
    new_nums = sorted(old_nums, key=lambda x: x % 2, reverse=True)
    print(new_nums)

def fun_reduce():
    old_nums = [35, 12, 8, 99, 60, 52]
    new_nums = reduce(lambda x, y: x + y, old_nums)
    print(new_nums)

def fun_zip():
    old_nums = [35, 12, 8, 99, 60, 52]
    # range(len(old_nums)) 从0开始的索引，
    # zip 函数将 old_nums 和索引序列按位置配对，生成一个元组的可迭代对象 new_nums，每个元组包含一个元素及其对应的索引。
    new_nums = zip(old_nums, range(len(old_nums)))
    print(list(new_nums))

# ****************偏函数****************
# 通过偏函数，可以固定某些函数的部分参数，从而生成一个新的函数。
def fun_partial():
    int2 = functools.partial(int, base=2)
    int8 = functools.partial(int, base=8)
    print(int('1001'))
    print(int2('1001'))
    print(int8('1001'))
    pass

# ****************装饰器****************
# 参数，返回值都是一个函数
def fun_decorator(func):
    """
    python 标准库functools模块的wraps函数也是一个装饰器，
    我们将它放在wrapper函数上，这个装饰器可以帮我们保留被装饰之前的函数，
    这样在需要取消装饰器时，可以通过被装饰函数的__wrapped__属性获得被装饰之前的函数。
    @wraps(func) 对应调用 func.__wrapped__(args)
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')
    return wrapper

@fun_decorator
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

@fun_decorator
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# ****************递归调用****************



if __name__ == '__main__':
    download('xxxx')
    download.__wrapped__('不记录时间：xxxx')