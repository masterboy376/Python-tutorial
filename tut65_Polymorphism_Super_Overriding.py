class A:
    classVarA='i am a class variable in class A'
    def __init__(self):
        self.varA='i am inside class A constructor'
        self.classVarA='i am a instance variable in class A'
        self.constant = 'Constant'
class B(A):
    classVarA='i am a class variable in class B'
    def __init__(self):
        super().__init__()
        # these two have been overrided
        self.varA='i am inside class B constructor'
        self.classVarA='i am a instance variable in class B'

a = A()
b = B()

print(b.classVarA)# first priority is always the instance variable(Whether in child or parent class)
print(b.constant)
