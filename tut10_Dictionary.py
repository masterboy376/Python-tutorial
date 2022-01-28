# dictionry means object
dictionary = {
    "sam":1023204142,
    "pym":124234254,
    "san":1432414143,
    "mad":24324324234,
    'world':{
        'a':1,
        "b":2
    }
}
print(dictionary)
print(dictionary["sam"])
print(dictionary["pym"])
print(dictionary["san"])
print(dictionary["mad"])
print(dictionary["world"])
print(dictionary["world"]["a"])
print(dictionary["world"]['b'])

dictionary['sambhav']=934241122315
#OR
dictionary.update({"leena":"toffee"})

print(dictionary)

del dictionary['world']

print(dictionary)

#===================================

d1= dictionary; # any change in d1 will change dictionary
d1= dictionary.copy(); # any change in d2 will not change dictionary

print(dictionary.keys());
print(dictionary.items());

