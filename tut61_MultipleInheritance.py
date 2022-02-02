class Employee:
    def __init__(self, name, role, age, salary):
        self.name = name
        self.age = age
        self.role= role
        self.salary = salary

    @staticmethod
    def printStr():
        print('Employee')    


class Entreprenuer:
    def __init__(self, name, age, networth, company):
        self.name = name
        self.age = age
        self.networth= networth
        self.company = company

    @staticmethod
    def printStr():
        print('Entreprenuer')    

class Programmer(Employee, Entreprenuer):# here the order is important: the constructor for arrguments will be searched in the Employee class
    def __init__(self, name, role, age, salary, language):
        super().__init__(name, role, age, salary)
        self.language = language

sam = Programmer('Sambhav Kaushik', 'brogrammer', 17, 99999999999, ['java','js','python','c++','dart']);
print(sam.language)
sam.printStr()# first class will be choosen first, then second class
