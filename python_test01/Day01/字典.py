"""
字典
"""
def dict_create():
    """
    创建字典
    :return:
    """
    # 方式一
    dict_a = {'name': 'alex', 'age': 18, 'sex': 'male'}
    print(dict_a)

    # 方式二
    dict_b = dict(name='alex', age=18, sex='male')
    print(dict_b)

    # 方式三
    dict_c = dict([('name', 'alex'), ('age', 18), ('sex', 'male')])
    print(dict_c)

    # 方式四
    # 可以通过Python内置函数zip压缩两个序列并创建字典
    dict_d = dict(zip('ABCDE', '12345'))
    print(dict_d)
    dict_e = dict(zip('ABCDE', range(1,10)))
    print(dict_e)
    #，** 符号用于解包字典（dictionary unpacking）。具体来说，** 可以将一个字典中的键值对解包并传递给另一个字典或函数
    dict_f = dict(zip('ABCDE', range(1,10)), **{'F': 10})
    print(dict_f)

    # 创建空字典
    dict_g = dict()
    print(dict_g)

    # 方式五
    dict_h = dict.fromkeys(['name', 'age', 'sex'], 'alex')
    print(dict_h)

    #方式六
    dict_i = {x: x*3 for x in range(1, 10)}
    print(dict_i)

    # 长度
    print(len(dict_i))

    # 遍历字典
    for key in dict_i:
        print(key)
    for key, value in dict_i.items():
        print(key, value)

def dict_method():
    person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
    print('name' in person)
    print(person['name'])
    person['name'] = 'alex'
    print(person['name'])
    # print(person['name222']) # KeyError
    print(person.get('name'))
    print(person.get('name222','default'))
    print(person.get('name222')) #None
    print('--------------------')
    print(person.keys())
    print(person.values())
    print(person.items())
    print('-------------------')
    person1 = {'name': '王大锤', 'age': 55, 'height': 178}
    person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
    person1.update(person2) # 有的直接更新，没有的更新
    print(person1)
    print('-------------------')
    person1.pop('age') #KeyError
    print(person1)
    person1.popitem()
    print(person1)
    del person['age'] #KeyError
    person.clear()

if __name__ == '__main__':
    dict_method()