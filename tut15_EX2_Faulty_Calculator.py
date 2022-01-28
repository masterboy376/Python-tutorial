# 45*3 = 555, 56+9 = 77, 56/6=4

a  = int(input())
b  = int(input())
operation = input();

if ((a==45 and b==3 and operation=='x') or (a==3 and b==45 and operation=='x')):
    print(555)
elif ((a==56 and b==9 and operation=='+') or (a==9 and b==56 and operation=='+')):
    print(77)
elif (a==56 and b==6 and operation=='/'):
    print(4)
elif (operation=='+'):
    print(a+b)
elif (operation=='-'):
    print(a-b)
elif (operation=='x'):
    print(a*b)
elif (operation=='/'):
    print(a/b)