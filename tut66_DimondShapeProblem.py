# this is no a problem in python, but it is in some other languages. Therefor multiple inheritance dhould be avoided. 
# use single and multilevel inheritance only 

class A:
    def met(self):
        print('this is a method from A')
class B(A):
    def met(self):
        print('this is a method from B')
class C(A):
    def met(self):
        print('this is a method from C')
class D(B, C):
    pass 

a = A()
b = B()
c = C()
d = D()

d.met()