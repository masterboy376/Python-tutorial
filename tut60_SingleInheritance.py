from pydoc import classname


class Employee:
    no_of_leaves = 30

    #----constructor OR __init__(self)----
    def __init__(self, name, role, age, salary):
        self.name = name
        self.age = age
        self.role= role
        self.salary = salary

    #----self----
    def printDetails(self):
        print(f"name is {self.name}")
        print(f"no of leaves is {self.no_of_leaves}")

    @classmethod
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))# arg

    @staticmethod
    def printStr(str):
        print(str)


class Programmer(Employee):
    def __init__(self, name, role, age, salary, language):
        super().__init__(name, role, age, salary)
        self.language = language
    no_of_leaves = 60


sam1 = Employee("sambhav kaushik", "all", 17, 9999999999999)
print(sam1.no_of_leaves)
sam2 = Programmer("sambhav kaushik", "programmer", 17, 9999999999999, ['java','js','python','c++','dart'])
print(sam2.no_of_leaves)
print(sam2.language)