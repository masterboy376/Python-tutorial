# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

# class Shape(metaclass=ABCMeta): # will define a template class for other classes : baseclass
class Shape(ABC): # for python version above 3.4
    @abstractmethod # this is a compulsary method for its child class
    def area(self):
        return 0
        #cannot create the object directly

class Rectangle(Shape):
    type='Rectangle'
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length*self.breadth 

rect1 = Rectangle(142,242)        
print(rect1.area())