a = 4;
b = 6;

# built-in function 
c = sum((a,b,4)); # list or tuple
print(c);

# function
def func1(a,b):
    print('hello, you are in func1, this function returns the remainder for two number');
    return a%b;

remainder = func1(3,3);
print(remainder); 

# docString
def avg(a,b):
    # """This function returns the average of two numbers."""
    
    """This function does not work for three numbers."""
    avg = (a+b)/2
    return avg;

print(avg.__doc__);



