"""
Iterable - iter() or __getitem__()
Iterator - __next__()
Iteration - process of using Iterator
"""

def gen(n): # this is generator
    for i in range(n): #range is a generator
        yield i # will generate the value on the fly

g = gen(3);
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# # print(g.__next__()) -->  no more iteration --> bcoz generator is iteratable only once

for i in g:
    print(i)

string = 'sambhav'
print(string.__iter__()) 
ier = iter(string)
print(ier.__next__())

# inte = 2344
# print(inte.__iter__()) --> not defined 

# quiz 
print('-------------------quiz-----------------')
def factorialGen(n):
    fact=1
    for i in range(1,n+1):
        fact*=i 
    yield fact

factorial = factorialGen(5)
for i in factorial:
    print(i)

def fibonacciGen(n):
    a,b = 0,1
    for i in range(n):
        yield a 
        a,b = b, b+a

fibonacci = fibonacciGen(5)
for i in fibonacci:
    print(i)

