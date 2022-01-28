# a, b, c, d are arguments
def func(a,b,c,d):
    print(a,b,c,d);
func("sam", "pym", "mad", "san")

# *args and 
def funcargs(normal, *args, **kw):
    print(normal);
    for item in args:
        print(item,'\n')
    for item in kw:
        print(item,'\n')

funcargs("sam", *["pym", "mad", "san"], **{'a':1,'b':2,'c':3,'d':4,'e':5}) #normal first and then args and then kwargs, args and kwargs are optional

