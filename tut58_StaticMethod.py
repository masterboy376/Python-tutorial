class Employee:
    no_of_leaves = 30

    #----constructor OR __init__(self)----
    def __init__(self, name, role, age, salary):
        self.name = name
        self.age = age
        self.role= role
        self.salary = salary

    #----self----
    def printDetails(self):# self is the object(instance) on which this function is being applied
        print(f"name is {self.name}")
        print(f"no of leaves is {self.no_of_leaves}")

    @classmethod # this will change the class variables
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod # this will change the class variables
    def from_str(cls, string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0], param[1], param[2], param[3])
        return cls(*string.split("-"))# arg

    @staticmethod
    def printStr(str):
        print(str)

# creating object using constructor
sam= Employee("Sam", "All", 17, 999999999999999)
pym= Employee("Pym", "All", 19, 459209042093)
kath= Employee.from_str('Kath-All-24-10000000')
print(sam)

sam.change_leaves(0);

print(kath.name)

Employee.printStr('hello')
sam.printStr('hello')



