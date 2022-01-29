# map 
number = ["1","4","934","65"]

# for i in range(len(number)):
#     number[i]=int(number[i])

# OR 

print(map(int, number))
number = list(map(int, number)) # map returns a object

number = list(map(lambda x:x*x, number))

print(number) 

def square(a):
    return a*a
def cube(a):
    return a*a*a

func = [square,cube]

for item in number:
    val = list(map(lambda x:x(item), func))
    print(val)

#---------------------------------------------------------
#filter
num = [ 1,25,465,2,5,34,3]

def isGreaterThanFive(num):
    return num>=5

newList=list(filter(isGreaterThanFive, num))
print(newList)

#----------------------------------------------------------
#reduce
from functools import reduce; # the function in reduce take two list item comutatively

n = [1,2,3,4]

# sum = 0 
# for item in n :
#     sum = sum + item
# print(sum)

#or

sum = reduce(lambda x,y:x+y , n);
print(sum)