# == : value equality : two object with same value
# is : reference equality : two object refer to a particular value

from re import A


a = [1,2,3,4]
b=a 
print (a is b)
print (a == b)
b[0]=0
print(a)

c = [1,2,3,4,5]
# d = [1,2,3,4,5]
d = c[:]
print (c is d)
print (c == d)
c[0]=0
print(d)