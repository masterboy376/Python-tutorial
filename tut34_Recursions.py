# means using function inside functions 

def factorialItrative(n):
    fac=1;
    for i in range (0,n):
        fac = fac * (1+i);
    return fac;

def factorialRecursive(n):
    if (n==1):
        return 1;
    else:
        return n*factorialRecursive(n-1);      

inp = int(input('Enter your number'));

print('Factorial using itrative method ', factorialItrative(inp));
print('Factorial using recursive method ', factorialRecursive(inp));


# Quiz: fibonacci series-> 0,1,1,2,3,5,8,13 
def fib(n):
    if (n==1):
        return 0;
    elif(n==2):
        return 1;
    else:
        return fib(n-1)+fib(n-2);

inp1 = int(input('Enter your number'));
print('fibonacci ', fib(inp1))
