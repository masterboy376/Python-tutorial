s_from_list = set([1,2,3,4]);
print(type(s_from_list), s_from_list);

s = set();
print(type(s));
# s.add({"a":1,'b':2}); -> cannot add dictionary
# s.add([1,2,3,4]); -> cannot add list
# s.add(True); -> cannot add boolean 
s.add(1);
s.add(2);
s.add(3);
s.remove(3);
print(s);

s1 = s.union([1,2,3]);
print(s, s1)

s2 = s.intersection([1,2,3]);
print(s, s2)

print(len(s))
print(max(s))
print(min(s))

# set does not contain a duplicate value
booleanSet1 = set([True, False, 1]);
booleanSet2 = set([1, False, True]);
print(booleanSet1); # {False, True}
print(booleanSet2); # {False, 1}
# this is because in python 1 == True & 0 == False OR hash(1) == hash(True) & hash(0) == hash(False)
print(0==False);
print(1==True);