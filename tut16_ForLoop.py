list = [['sam',1],['pym',2],['rym',3],['kath',4]] #itratable
tpl = (['sam',1],['pym',2],['rym',3],['kath',4]) #itratable
dict = dict(list)
# dict = dict(tpl) -> not possible

#list or tuple
for person, number in tpl:
    print(person, number)

#dictionary
for person, number in dict.items():
    print(person, number)
for person in dict:
    print(person, number)


# quiz
list1= [1,6,'sam',{'r':1,'p':2},[True,False],-1,0.8]

for item in list1:
    if type(item)==int or type(item)==float :
        print(item)