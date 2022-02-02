class Employee:
    no_of_leaves = 30

    def __init__(self, name, role, age, salary):# This is dunder method: always run when object will be created
        self.name = name
        self.age = age
        self.role= role
        self.salary = salary

    def printDetails(self):
        print(f"name is {self.name}")
        print(f"no of leaves is {self.no_of_leaves}")

    @classmethod
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printStr(str):
        print(str)

    def __add__(self, other):# This is dunder method: always run addition operation is used: it is operator overloading
        return self.age + other.age    
    # search : mapping operators to functions on google 

    def __repr__(self):# should return a string
        return (f'name: {self.name}, role:{self.role}, age:{self.age}, salary:{self.salary}')
    def __str__(self):# should return a string -----> this will be the first priority
        return f"Employee('{self.name}', '{self.role}, {self.age}, {self.salary}')"

emp1 = Employee('Sam','programmer',17,423523423242)
emp2 = Employee('Kath','programmer',24,4235234)

print(emp1+emp2)

print(emp1)