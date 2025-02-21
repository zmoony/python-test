""""
函数和模块
* 之后必须是强制关键字
/ 之前的顺序不可更改
"""
import random
import string


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

if __name__ == '__main__':
    print(calc(1, calc_add, 2, 3, a=1, b=2))
    print(calc(9, calc_sub, 2, 3, a=1, b=2))