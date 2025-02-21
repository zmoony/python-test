"""
if else
match case (>= 3.10.x)
"""

def if_test():
    height = float(input("请输入身高："))
    weight = float(input("请输入体重："))
    """
    括号 () 具有最高优先级，先计算括号内的表达式。
    幂运算 ** 的优先级高于除法 /，因此在括号内的表达式中，先进行幂运算。
    除法 / 在幂运算之后进行。
    """
    bmi = weight / (height / 100) ** 2
    print(f'{bmi = :.1f}')
    if 18.5<=bmi<24.9:
        print('正常')
    elif bmi < 18.5:
        print('你的体重过轻！')
    elif bmi < 27:
        print('你的体重过重！')
    elif bmi < 30:
        print('你已轻度肥胖！')
    elif bmi < 35:
        print('你已中度肥胖！')
    else:
        print('不正常')

def match_test():
    status_code = int(input("请输入状态码："))
    match status_code:
        case 200 | 201:
            print("OK")
        case 404:
            print("NOT FOUND")
        case 500:
            print("INTERNAL SERVER ERROR")
        case _:# 可选 其他的都会进来
            print("UNKNOWN")

if __name__ == '__main__':
    match_test()


