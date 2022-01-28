# l =10 # this variable is globally available for this file
# # note you can not change global variable inside a func or any other block -> for this we use global keyword
# def func():
#     # l = 5 # this variable is locally available for this function
#     global l 
#     l = l +40
#     print(l, 'local')

# func();
# print(l, 'global')

x=88
def func1():
    x = 20 # this is not a global variable 
    def func2():
        global x 
        x=100
    print('before calling func2', x)    
    func2()
    print('after calling func2', x)       

func1()
print(x, "global")