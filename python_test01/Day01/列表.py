"""
列表
items3 = [100, 12.3, 'Python', True] 一般不建议，建议同类型的放到一起
可以有重复元素，不同类型
使用list函数构建
"""
import random


def list_test():
    items = [1, 2, 3, 4, 5]
    items = list(range(1, 6))
    item_str = list('hello')  # 变成了char[]
    print(items)
    print(item_str)
    pass


def list_merge():
    items1 = [1, 2, 3, 4, 5]
    items2 = [6, 7, 8, 9, 10]
    # 两个列表合并
    items3 = items1 + items2
    items1 += items2
    print(items3)
    print(items1)
    # 指定次数重复
    print(items1 * 2)
    pass


def list_exists():
    items1 = [1, 2, 3, 4, 5]
    if 1 in items1:
        print('存在')
    else:
        print('不存在')
    print(1 in items1)
    print(1 not in items1)


def list_index():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    # 查找索引
    print(items8.index('apple'))
    try:
        print(items8.index('banana'))
    except ValueError:
        print('不存在')
    # 正向索引 0~N-1
    print(items8[0])
    # 负向索引 -1~-N
    print(items8[-1])
    # 切片[start:end:stride] [START,END)
    # 如果start值等于0，那么在使用切片运算符时可以将其省略；
    # 如果end值等于N，N代表列表元素的个数，那么在使用切片运算符时可以将其省略；
    # 如果stride值等于1，那么在使用切片运算符时也可以将其省略。
    print(items8[0:3])
    print(items8[1:4:12])
    print(items8[-1:-4:-1])
    # 修改元素，将索引1-2的元素替换成x,o
    items8[1:3] = ['x', 'o']
    print(items8)
    # 删除元素，删除索引1-2的元素
    del items8[1:3]
    print(items8)
    # 删除元素，删除索引1-2的元素
    items8.remove('apple')
    print(items8)
    # 指定索引的值
    print(items8[0])
    print(items8.index('watermelon'))
    items8.insert(1, 'orange')
    items8.insert(5, 'orange')
    print(items8)
    print("----------")
    print(items8.index('peach', 1))  # 之后的索引没有会异常ValueError
    pass


def list_equals():
    items1 = [1, 2, 3, 4, 5]
    items2 = list(range(1, 6))
    print(items1 == items2)  # true
    print(items1 is items2)  # false
    print(items1 is not items2)  # true
    pass


def list_sort():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    items8.sort()
    print(items8)


def list_reverse():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    items8.reverse()
    print(items8)


def list_copy():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    items9 = items8.copy()
    print(items9)
    items8.append('banana')
    print(items8)
    print(items9)


def list_clear():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    items8.clear()
    print(items8)


def list_append():
    """
    append 添加元素，
    insert插入元素，
    extend扩展元素，
    pop删除元素，最后一个元素 IndexError 超出索引
    remove删除元素，ValueError 需要做存在判断。只会删除第一个
    clear清空元素
    :return:
    """
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    items8.pop(1)  # 指定index
    print(items8)
    items8.append('banana')
    items8.insert(1, 'banana')
    print(items8)
    items8.remove('banana')  # 只会删除第一个
    print(items8)
    items8.insert(1, 'orange')
    print(items8)
    items8.extend(['grape', 'pear'])
    print(items8)
    items8.pop()
    print(items8)
    items8.pop(1)
    print(items8)
    del items8[1]  # 性能不如pop，可以忽略
    print(items8)


def list_count():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    print(items8.count('apple'))
    print(items8.count('banana'))
    print(items8.count('apple'))
    print(items8.count('banana'))
    print(items8.__len__())
    print(len(items8))


def list_loop():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    for item in items8:
        print(item)
    print('--------------------------')
    for i in range(len(items8)):
        print(items8[i])


def list_create():
    """
    创建一个取值范围在1到99且能被3或者5整除的数字构成的列表
    :return:
    """
    items = []
    for i in range(1, 100):
        if i % 3 == 0 or i % 5 == 0:
            items.append(i)
    print(items)
    print('------------------------')
    items2 =[i for i in range(1,100) if i % 3 == 0 or i % 5 == 0]
    print(items2)
    items3 = [i**2 for i in items]
    print(items3)
    items4 = [i for i in items if i >= 50]
    print(items4)
    pass

def list_multidimensional():
    """
    通过产生随机数的方式来生成5个学生3门课程的成绩并保存在列表
    :return:
    """
    items = [[random.randrange(60,100) for _ in range(3)] for i in range(5)]
    print(items)

if __name__ == '__main__':
    list_multidimensional()
