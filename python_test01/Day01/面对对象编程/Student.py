class Person:
    def __init__(self, color, eye):
        self.color = color
        self.eye = eye

    def eat(self):
        print(f"{self.color}的{self.eye}眼睛正在吃东西")

    def sleep(self):
        print(f"{self.color}的{self.eye}眼睛正在睡觉")

class Student(Person):
    """
    继承
    构造方法里面写super().__init__()
    """
    # 禁止后面动态添加属性
    # __slots__ = ('name', 'age')

    def __init__(self, name, age, gender, color, eye):
        """初始化方法
        _name 受保护的，访问需要开方法，相当于get/set
        __gender 私有变量
        """
        super().__init__(color, eye)
        self._name = name
        self.age = age
        self.__gender = gender

    @staticmethod
    def static_method(name, age):
        """
        静态方法
        第一个参数不是self
        对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，
        区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象
        :param name:
        :param age:
        :return:
        """
        print(f"静态方法={name}正在学习{age}")

    @classmethod
    def class_method(cls, name, age):
        """
        类方法
        第一个参数是cls，代表类本身，而不是实例对象
        :param name:
        :param age:
        :return:
        """
        print(f"类方法={name}正在学习{age}")


    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")

    def play(self):
        print(f"{self.name}正在打游戏")

    @property
    def name(self):
        """
        @property 可以将方法变成属性，直接可以Student.func(*args)就可以了
        :return:
        """
        return self._name


"""
定义类、创建对象、给对象发消息
"""
if __name__ == '__main__':
    stu1 = Student("小明", 18, "男")
    # stu1.study("Python")
    # stu1.play()
    stu2 = Student("小红", 17, "女")
    print(stu1.name)
    print(stu1._Student__gender) #也能访问到
    # python本身是动态语言，所以可以动态添加属性
    stu1.address = "北京"
    print(stu1.address)
    # 相同的内存地址
    # print(hex(id(stu1)))
    # print(hex(id(stu2)))
    # print(stu1.play())
    # print(Student.study(stu1, "Python"))
    # print(stu2 == stu1)  #False
    # print(id(stu1) == id(stu2)) #False
    # print(hex(id(stu1)) == hex(id(stu2))) #False
    print(Student.static_method('小明',32))
    print(Student.class_method('小明',32))