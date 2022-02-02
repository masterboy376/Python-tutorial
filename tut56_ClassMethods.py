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

# sam = Employee()
# sam.name = "Sambhav"
# sam.no_of_leaves = 0
# pym = Employee()
# pym.name= "priyam"
# pym.no_of_leaves = 45
# sam.printDetails()# sam will automatically become the argument of printDetails()
# pym.printDetails()

# creating object using constructor
sam= Employee("Sam", "All", 17, 999999999999999)
kath= Employee("Kath", "All", 24, 999999999999999)
pym= Employee("Pym", "All", 19, 999999999999999)
print(sam)

sam.change_leaves(0);
print(Employee.no_of_leaves)

