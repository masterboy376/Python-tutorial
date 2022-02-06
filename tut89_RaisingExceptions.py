# 1
# a = input('enter your beautiful name ')
# if a.isnumeric():
#     raise Exception("Numbers are not allowed as a name.")
# print(f".......Hello {a}..........")    
# # assum this below code takes 1 hour to run so check the input before

# 2
# a = int(input('Enter first number '))
# b = int(input('Enter second number '))
# if a is 0:
#     raise ZeroDivisionError('this operation will be undefined')
# print(f'b/a is {b/a}')

# 3
c = input('Name please ')
try:
    print(a)
except Exception as e:
    if c == 'sam':
        raise ValueError('sam is not allowed to login')
    print(f'Error: variable is not defined')