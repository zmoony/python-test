import json

"""
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

实际环境中，一般使用ujson代替
"""

def json_dumps():
    """
    将字典处理成JSON格式（以字符串形式存在）
    ensure_ascii : 默认为True，表示输出的JSON字符串中不能出现中文，必须使用ASCII编码，如果为False，则输出的JSON字符串可以包含中文
    indent: 缩进空格数，默认为None，表示不缩进，如果为整数，则表示缩进空格数，如果为字符串，则表示缩进字符串
    :return: 返回一个JSON格式的字符串
    """
    my_dict = {
        'name': '骆昊',
        'age': 40,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BMW', 'max_speed': 240},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 280}
        ]
    }
    print(json.dumps(my_dict, ensure_ascii=False, indent=4))

def json_dump():
    """
    将Python对象（如字典、列表等）直接写入到文件中，以JSON格式存储
    :return: 无返回值，直接将内容写入文件。
    """
    my_dict = {
        'name': '骆昊',
        'age': 40,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BMW', 'max_speed': 240},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 280}
        ]
    }
    with open('data.json', 'w', encoding='utf-8') as fs:
        json.dump(my_dict, fs, ensure_ascii=False, indent=4)

def json_load():
    """
    从文件中读取JSON格式的内容，并解析为Python对象
    :return: 返回一个Python对象
    """
    with open('data.json', 'r', encoding='utf-8') as fs:
        my_dict = json.load(fs)
        print(my_dict)
        print(type(my_dict))

if __name__ == '__main__':
    json_load()