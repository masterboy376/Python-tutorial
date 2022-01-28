import math
import time

print(time.time_ns())
me = 'sambhav kaushik'
a1 = 1

# cumbersome method
# str = "this is %s %s"%(me, a1);
# print(str)

#mordern method
# str1= "this is {} {}",
# b = str1.format(me,a1)
# print(b)

# this is f-strings 
str2= f"this is {me} {a1} {math.cos(90)}"
print(str2);
print(time.time_ns())





