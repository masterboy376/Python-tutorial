# list on number divisible by 3 
# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)


# list comprehensions 
ls=[i for i in range(100) if i%3==0] # ls = [tobeappended what conditiontobefullilled(optional)]
print(ls)

# dictionary comprehensions 
dict = {i:f"item{i}" for i in range(10) if i%2==0}
# reversing the dictionary
dict1 = {value:key for key,value in dict.items()}
print(dict, dict1)

# set comprehensions
dresses = {dress for dress in ['d1','d2','d3','d4','d3','d1']}
print(dresses)

# generator comprehensions 
evens = (i for i in range(101) if i%2==0)
for item in evens :
    print(item, end=' ')
print()
# quiz 
lst = list(input())
comtype = input()
if(comtype == 'list'):
    l=[i for i in lst] 
    print(l)
elif(comtype == 'dic'):
    d = {i:f"item{i}" for i in lst}
    print(d)
if(comtype == 'set'):
    s={i for i in lst}
    print(s)