class Employee:
    no_of_leaves = 30
    pass

sam = Employee()
sam.name = "Sambhav"
sam.no_of_leaves = 0
pym = Employee()
pym.name= "priyam"
pym.no_of_leaves = 45

Employee.no_of_leaves = 31

print(f"instance variables {sam.name} and {pym.name} and {sam.no_of_leaves} and {pym.no_of_leaves}")
print(f"class variables {Employee.no_of_leaves}")