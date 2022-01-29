# modify the functioning of a function 

# def func1():
#     print('my name is gon')

# func2 = func1
# del func1 # delete func1

# func2()

# def function(n):
#     if n==0:
#         return print
#     if n == 1:
#         return int 

# a = function(0)
# print(a)

# def executor(func, inp):
#     func(inp)

# executor(print, "i am sam")

# decorators 
def dec1(func):
    def nowExec():
        print("executing now")
        func()
        print("executed")
    return nowExec

@dec1
def whoIsSam():
    print('sam is bro grammer')

#whoIsSam = dec1(whoIsSam) # or use @ mark
whoIsSam()