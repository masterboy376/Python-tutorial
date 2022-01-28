minus = lambda x,y: x-y;
print(minus(9,19))

# sort 
def a_first(a):
    return a[1];
a = [[1,50],[6,8],[0,5]];
#a.sort(key = a_first);# by defauly key = a[0]
a.sort(key = lambda x:x[1]);# by defauly key = a[0]
print(a)