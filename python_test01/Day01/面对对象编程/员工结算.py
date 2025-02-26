from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算薪资"""
        pass

class Manager(Employee):
    """部门经理"""
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""
    def __init__(self, name, working_hour = 0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200.0 * self.working_hour

class Salesman(Employee):
    """销售"""
    def __init__(self, name, sales = 0.0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


if __name__ == '__main__':
    emps = [Manager('Tom'), Programmer('Bob'), Salesman('Alice')]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = 5
        elif isinstance(emp, Salesman):
            emp.sales = 1000
        print('%s: %s' % (emp.name, emp.get_salary()))




















