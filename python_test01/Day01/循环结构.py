"""
循环结构
"""
import time


def for_in_test():
    """
    每隔1秒输出一次“hello, world”，持续1小时
    range(101)  0-100
    range(0,101) [0,101)
    range(0,101,2) 步长2
    range(101,0,-2) 步长-2
    for 里面的变量没有用到，可以直接使用_代替
    :return:
    """
    for _ in range(60 * 60):
        print("hello, world")
        time.sleep(1)


def while_test():
    """
    从1到100的整数求和
    break 跳出当前循环
    continue 跳过当前循环
    """
    i = 1
    total = 0
    while i <= 100:
        total += i
        i += 1

if __name__ == '__main__':
    while_test()
