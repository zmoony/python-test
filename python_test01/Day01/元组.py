"""
元组
不可更改 -- 使用多线程
"""
def tuple_create():
    t1 = (1, 2, 3, 4, 5)
    t2 = ('骆昊', 43, True, '四川成都')
    print(t1)
    print(t2)
    # 查看变量类型
    print(type(t1))
    print(type(t2))
    # 查看数量
    print(len(t1))
    print(len(t2))
    # 访问元素
    print(t1[0])
    print(t1[-1])
    print(t2[0])
    print(t2[-1])
    # 访问切片
    print(t1[:3])
    print(t2[::3])
    # 遍历
    for item in t1:
        print(item)
    # 存在
    print(43 in t2)
    # 修改元组--TypeError
    try:
        t1[0] = 100
    except TypeError as e:
        print(e)
    # 拼接
    t3 = t1 + t2
    print(t3)
    # 单个元组需要加个一个逗号，与str,int进行区分
    t4 = (1,)
    print(type(t4)) #tuple
    t5 = (1)
    print(type(t5)) #int
    # 解构赋值（打包解包）数量需要对应，要不然会报错。可使用*代替，代表一个e[]
    a, b, c, d, e = t1
    print(a, b, c, d, e)
    t8 = 1,2,3
    print(t8) #tuple
    a, *b = t1
    print(a, b) #1 [2, 3, 4, 5]
    a, b, *c = range(0,10)
    print(a, b, c) #0 1 [2, 3, 4, 5, 6, 7, 8, 9]
    a, b, c = [1,2,3]
    print(a, b, c)
    a, *b, c = 'hello'
    print(a, b, c) # h ['e', 'l', 'l'] o
    pass

def change_value():
    a,b,c=(1,2,3)
    a,b,c = b,c,a
    print(a,b,c)

def list_tuple():
    infos = ('骆昊', 43, True, '四川成都')
    # 将元组转换成列表
    print(list(infos))  # ['骆昊', 43, True, '四川成都']

    frts = ['apple', 'banana', 'orange']
    # 将列表转换成元组
    print(tuple(frts))  # ('apple', 'banana', 'orange')

if __name__ == '__main__':
    list_tuple()