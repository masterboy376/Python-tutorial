# Arithmatic operators
from ast import operator


print(1+9);
print(1-9);
print(1*9);
print(2**4); # 2 to the power 4
print(1/9);
print(1//9); # this will return the integer value only -> floar division operator
print(5%5); # this will return the remainder

# Assignment opera;tors
num = 7;
print(num);
num +=2;
print(num);
num -=1;
print(num);
num *=2;
print(num);
num /=1;
print(num);
num //=1;
print(num);
num %=7;
print(num);
num **=3;
print(num);

# Comparision operators
print(1==2);
print(1!=2);
print(1<=2);
print(1>=2);
print(1>2);
print(1<2);

# Logical operator
a=True;
b=False;
print(a and a);
print(a and b);
print(b and b);
print(a or a);
print(a or b);
print(b or b);

# Identity operator 
print(a is b);
print(b is b);
print(a is a);
print(a is not b);
print(a is not a);
print(b is not b);

# Membership operator
list = [1,23,56,5];
print(4 in list);
print(4 not in list);
print(23 in list);
print(23 not in list);

# Bitwise operator
# 0 -> 00
# 1 -> 01
# 2 -> 10
# 3 -> 11

print (0 & 1);
print (0 | 1);
print (0 & 3);
print (0 | 3);
print (0 & 2);
print (0 | 2);
print (1 & 2);
print (1 | 2);









