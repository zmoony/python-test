"""
集合 set
无序性, 互异性, 确定性
"""
def set_create():
    set1 = {1,1,12,3} #去重
    print(set1)
    set2 = set('hello')
    print(set2)
    set3 = set([1,2,3,4,5])
    set4 = {num for num in range(10) if num % 2 == 0}
    print(set3)
    print(set4)

def set_loop():
    set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    for item in set1:
        print(item)

def set_exists():
    set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    print('Python' in set1)

def set_calculation():
    set1 = {1, 2, 3, 4, 5, 6, 7}
    set2 = {2, 4, 6, 8, 10}
    # 交集
    print(set1 & set2)
    print(set1.intersection(set2))
    # 并集
    print(set1 | set2)
    print(set1.union(set2))
    # 差集（只展示了set1的）
    print(set1 - set2)
    print(set1.difference(set2))
    # 对称差（所有不一样的都展示出来）
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))
    # 子集
    print(set1 <= set2)
    # 超集
    print(set1 >= set2)
    # 子集
    print(set1.issubset(set2))
    # 超集
    print(set1.issuperset(set2))
    print('----------------')
    set1 |= set2
    print(set1)
    # 判断两个集合有没有相同的元素
    # 判断两个集合有没有相同的元素，如果没有相同元素，该方法返回True，否则该方法返回False，代码如下所示。
    print(set1.isdisjoint(set2))

def set_add():
    set1 = {1, 2, 3, 4, 5, 6, 7}
    set1.add(8)
    print(set1)
    set1.update([9, 10, 11]) # 添加多个
    print(set1)
    set1.discard(1) # 不存在不报错
    print(set1)
    set1.remove(2) # 不存在报错 KeyError
    print(set1)

def frozenset_test():
    set1 = frozenset([1, 2, 3, 4, 5, 6, 7])
    set1 = frozenset({1,2,3})
    set1 = frozenset(range(1,6))
    print(set1)
    print(type(set1))

if __name__ == '__main__':
    set_calculation()