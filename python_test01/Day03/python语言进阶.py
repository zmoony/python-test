
"""
生成式（推导式）的用法 (用来生成列表、集合和字典。)
"""
import concurrent

from python_test01.Day01.函数和模块 import is_prime


def important_test():
    print('**********生成式************')
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key:value for key, value in prices.items() if value > 100}
    print('*********嵌套的列表的坑*********')
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    #分别录入成绩
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input('请输入%s的%s成绩：' % (name, course)))
            print(scores)

def heapq_test():
    """
    heapq模块（堆排序）
    从列表中找出最大的或最小的N个元素
    堆结构(大根堆/小根堆)
    :return:
    """
    import heapq
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

def itertools_test():
    """
    迭代工具模块
    :return:
    """
    import itertools

    # 产生ABCD的全排列
    i1 = itertools.permutations('ABCD')
    # for i in i1:
    #     print(i)
    # 产生ABCDE的五选三组合
    itertools.combinations('ABCDE', 3)
    # 产生ABCD和123的笛卡尔积
    itertools.product('ABCD', '123')
    # 产生ABC的无限循环序列
    itertools.cycle(('A', 'B', 'C'))

def collections_test():
    """
    namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
    deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素时，deque会表现出更好的性能，渐近时间复杂度为0(1)
    Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
    OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
    defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
    找出序列中出现次数最多的元素
    :return:
    """
    from collections import Counter
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3)) # 输出出现次数最多的3个元素

"""
排序算法
"""
def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

def bubble_high_sort(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)

def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)

def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


import threading

"""
正常类与元类的区别
1. 正常类的 __init__
运行时机：当通过类创建实例时调用。例如，当你执行 obj = MyClass() 时，MyClass.__init__ 方法会被调用。
作用：用于初始化新创建的对象，设置对象的属性和状态。
2. 元类的 __init__
运行时机：当定义继承该元类的子类时调用。例如，当你定义 class SubClass(metaclass=SingletonMeta) 时，SingletonMeta.__init__ 方法会被调用。
作用：用于初始化类本身，而不是类的实例。可以用来修改类的行为或添加类级别的属性。

正常类与元类的区别
1. 定义和作用
正常类：
定义：用于创建对象（实例）。每个类可以有多个实例，每个实例拥有独立的状态。
作用：封装数据和行为，提供属性和方法来操作这些数据。
元类：
定义：用于创建类。元类是类的类，即它控制类的创建过程。
作用：允许你在类定义时修改类的行为或结构，例如添加方法、属性，或者实现特定的设计模式（如单例模式）。
2. 创建时机
正常类：
创建实例时调用：当你通过类创建对象时，如 obj = MyClass()，会调用类的构造函数 __init__ 来初始化该对象。
元类：
定义子类时调用：当你定义一个继承自该元类的子类时，如 class SubClass(metaclass=MyMeta)，会调用元类的 __init__ 和 __new__ 方法来创建和初始化这个类本身。
3. 使用场景
正常类：
适用于大多数面向对象编程的需求，如封装数据、定义行为、继承和多态等。
元类：
适用于需要动态修改类的行为或结构的高级场景，如框架开发、设计模式实现（如单例模式）、自动注册类等。
4. 方法调用
正常类：
__init__ 方法在创建实例时调用，用于初始化实例属性。
__call__ 方法使类实例可以像函数一样被调用。
元类：
__init__ 方法在定义子类时调用，用于初始化类本身。
__call__ 方法在创建类实例时调用，可以控制实例的创建过程。

"""
class SingletonMeta(type):
    """自定义元类
    __init__ 方法初始化类时设置实例为 None 并创建一个可重入锁。
    __call__ 方法在创建类实例时检查是否已存在实例，若不存在则加锁并再次检查，确保线程安全地创建唯一实例。
    ，__init__ 在定义继承该元类的子类时运行，而 __call__ 在创建这些子类的实例时运行。
    """

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """总统(单例类)"""

    pass

"""
设计模式
创建型模式：单例、工厂、建造者、原型
结构型模式：适配器、门面（外观）、代理
行为型模式：迭代器、观察者、状态、策略
"""

"""
getattr 函数解释
getattr 是 Python 内置函数，用于从对象中获取指定名称的属性值。其基本语法如下：
getattr(object, name[, default])
name_value = getattr(obj, 'name', 'Default Name')
"""

class StreamHasher:
    """哈希摘要生成器"""

    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的摘要"""
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()

def StreamHasher_main():
    """主函数"""
    hasher1 = StreamHasher()
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher2(stream))

"""
迭代器
__iter__和__next__魔术方法就是迭代器协议
"""
class Fib(object):
    """迭代器"""
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()

def fib(num):
    """生成器
    yeild 先返回，下回从这个位置继续实行，这个返回的是11235的斐波那契数
    """
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter

def calc_avg_main():
    gen = calc_avg()
    next(gen)
    print(gen.send(10))
    print(gen.send(20))
    print(gen.send(30))

"""
并发编程
1. 多线程
Python中提供了Thread类并辅以Lock、Condition、Event、Semaphore和Barrier。
Python中有GIL（全局解释器锁）来防止多个线程同时执行本地字节码，这个锁对于CPython是必须的，因为CPython的内存管理并不是线程安全的，因为GIL的存在多线程并不能发挥CPU的多核特性。
2. 多进程
3. 异步I/O
"""

def multithreading():
    """
    面试题：进程和线程的区别和联系？
    进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
    线程 - 操作系统分配CPU的基本单位
    并发编程（concurrent programming）
    1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
    2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
    """
    import glob
    import os
    import threading
    from PIL import Image

    PREFIX = 'thumbnails'

    def generate_thumbnail(infile, size, format='PNG'):
        """生成指定图片文件的缩略图"""
        file, ext = os.path.splitext(infile)
        file = file[file.rfind('/') + 1:]
        outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
        img = Image.open(infile)
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(outfile, format)

    def thread_main():
        """
        glob.glob 是 Python 标准库 glob 模块中的一个函数，用于查找符合特定模式的文件路径。它会返回一个列表，包含所有匹配的文件路径字符串。常用通配符包括：
        *：匹配任意数量的任意字符
        ?：匹配单个任意字符
        [seq]：匹配 seq 中的任意一个字符
        [!seq] 或 [^seq]：匹配不在 seq 中的任意一个字符
        例如，glob.glob('*.py') 会返回当前目录下所有扩展名为 .py 的文件路径。
        :return:
        """
        if not os.path.exists(PREFIX):
            os.mkdir(PREFIX)
        for infile in glob.glob('../../data/processed/images/*.png'):
            # threading.Thread(target=generate_thumbnail, args=(infile, (100, 100))).start()
            for size in (32, 64, 128):
                # 创建并启动线程
                threading.Thread(
                    target=generate_thumbnail,
                    args=(infile, (size, size))
                ).start()


def multithreading_competition():
    """
    存在临界资源（资源竞争）
    :return:
    """
    import time
    import threading

    from concurrent.futures import ThreadPoolExecutor
    class Account(object):
        """银行账户"""

        def __init__(self):
            self.balance = 0.0
            self.lock = threading.Lock()
        #存款
        def deposit(self, money):
            # 通过锁保护临界资源
            with self.lock:
                new_balance = self.balance + money
                time.sleep(0.001)
                self.balance = new_balance

    def account_main():
        account = Account()
        # 创建线程池
        futures = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            for _ in range(100):
                future = executor.submit(account.deposit, 1)
                futures.append(future)
        for future in futures:
            future.result()
        print(account.balance)

def multithreading_competition_main():
    """
    多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
    多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
    多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
    """
    from concurrent.futures import ThreadPoolExecutor
    from random import randint
    from time import sleep

    import threading

    class Account:
        """银行账户"""

        def __init__(self, balance=0):
            self.balance = balance
            lock = threading.RLock()
            self.condition = threading.Condition(lock)

        def withdraw(self, money):
            """取钱"""
            with self.condition:
                while money > self.balance:
                    self.condition.wait()
                new_balance = self.balance - money
                sleep(0.001)
                self.balance = new_balance

        def deposit(self, money):
            """存钱"""
            with self.condition:
                new_balance = self.balance + money
                sleep(0.001)
                self.balance = new_balance
                self.condition.notify_all()
    def add_money(account):
        while True:
            money = randint(5, 10)
            account.deposit(money)
            print(threading.current_thread().name,
                  ':', money, '====>', account.balance)
            sleep(0.5)


    def sub_money(account):
        while True:
            money = randint(10, 30)
            account.withdraw(money)
            print(threading.current_thread().name,
                  ':', money, '<====', account.balance)
            sleep(1)


    def main():
        account = Account()
        with ThreadPoolExecutor(max_workers=15) as pool:
            for _ in range(5):
                pool.submit(add_money, account)
            for _ in range(10):
                pool.submit(sub_money, account)

"""
多进程
多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
"""

PRIMES = [
             1116281,
             1297337,
             104395303,
             472882027,
             533000389,
             817504243,
             982451653,
             112272535095293,
             112582705942171,
             112272535095293,
             115280095190773,
             115797848077099,
             1099726899285419
         ] * 5
def multiprocessing_test():
    import concurrent.futures
    import math

    def is_prime(n):
        """判断素数"""
        if n % 2 == 0:
            return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

def multiprocessing_test_main():
    """
    任务分配：map 方法会将 PRIMES 列表中的每个元素作为参数依次传递给 is_prime 函数，并将这些任务分配给进程池中的不同进程进行并行处理。
    结果收集：map 方法会按顺序返回每个任务的结果，即 is_prime 函数对每个数字的计算结果。即使任务是并行执行的，结果仍然会按照输入的顺序返回。
    异常处理：如果某个任务抛出异常，map 方法会在尝试获取该任务的结果时抛出相同的异常。
    :return:
    """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

"""
异步处理
从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。
异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序的不确定，因此需要通过回调式编程或者future对象来获取任务执行的结果。
Python 3通过asyncio模块和await和async关键字（在Python 3.7中正式被列为关键字）来支持异步处理。
"""
def async_test():
    import asyncio
    def num_generator(m, n):
        """指定范围的数字生成器
        yield：用于生成单个值，适合简单的生成器逻辑。
        yield from：用于将另一个生成器或可迭代对象的元素逐个产出，简化嵌套生成器的编写。
        def sub_generator():
            yield 'A'
            yield 'B'
            yield 'C'

        def main_generator():
            yield from sub_generator()  # 委托给子生成器
            yield 'D'

        gen = main_generator()
        for item in gen:
            print(item)
        """
        yield from range(m, n + 1)

    async def prime_filter(m, n):
        """素数过滤器"""
        primes = []
        for i in num_generator(m, n):
            flag = True
            for j in range(2, int(i ** 0.5 + 1)):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                print('Prime =>', i)
                primes.append(i)

            await asyncio.sleep(0.001)
        return tuple(primes)

    async def square_mapper(m, n):
        """平方映射器"""
        squares = []
        for i in num_generator(m, n):
            print('Square =>', i * i)
            squares.append(i * i)

            await asyncio.sleep(0.001)
        return squares

    async def main():
        """
        上面的代码使用get_event_loop函数获得系统默认的事件循环，
        通过gather函数可以获得一个future对象，
        future对象的add_done_callback可以添加执行完成时的回调函数，
        loop对象的run_until_complete方法可以等待通过future对象获得协程执行结果。
        :return:
        """
        loop = asyncio.get_event_loop()
        future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
        future.add_done_callback(lambda x: print(x.result()))
        loop.run_until_complete(future)
        loop.close()
"""
要实现任务的异步化，可以使用名为Celery的三方库。Celery是Python编写的分布式任务队列，它使用分布式消息进行工作，可以基于RabbitMQ或Redis来作为后端的消息代理。
"""
def aiohttp_test():
    """
    异步的HTTP客户端和服务器
    :return:
    """
    import asyncio
    import re

    import aiohttp
    PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')

    async def fetch_page(session, url):
        async with session.get(url, ssl=False) as resp:
            return await resp.text()

    async def show_title(url):
        async with aiohttp.ClientSession() as session:
            html = await fetch_page(session, url)
            print(PATTERN.search(html).group('title'))

    def main():
        urls = ('https://www.python.org/',
                'https://git-scm.com/',
                'https://www.jd.com/',
                'https://www.taobao.com/',
                'https://www.douban.com/')
        loop = asyncio.get_event_loop()
        cos = [show_title(url) for url in urls]
        loop.run_until_complete(asyncio.wait(cos))
        loop.close()

if __name__ == '__main__':
    collections_test()
    # print(5//3)
    # print(5/3)
    # print(5%3)

























