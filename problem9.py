"""
jumble the names
"""

import random


no_of_name = int(input('enter the total number of name: '))
print(f'enter the name of your {no_of_name} friend')
names = []
for i in range(no_of_name):
    names.append(list(input().split(" ")))

for i in range(no_of_name):
    r = random.randint(0,no_of_name)
    if r != i:
        print(f'{names[i][0]} {names[r][1]}')
    elif r == no_of_name-1:
        print(f'{names[i][0]} {names[r-1][1]}')
    else:
        print(f'{names[i][0]} {names[r+1][1]}')


