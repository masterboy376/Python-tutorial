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

# sam = Employee()
# sam.name = "Sambhav"
# sam.no_of_leaves = 0
# pym = Employee()
# pym.name= "priyam"
# pym.no_of_leaves = 45
# sam.printDetails()# sam will automatically become the argument of printDetails()
# pym.printDetails()

# creating object using constructor
sambhav= Employee("Sambhav Kaushik", "All", 17, 999999999999999)
print(sambhav)

