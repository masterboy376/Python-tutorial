a = 1
b = 20
inp = int(input());

if inp>=b:
    print('input is greater then equal to b');
elif inp<a:
    print('input is less than a');
else :
    print('non')    

#-----------------------------------------------------
# in terms of list
list = [3,4,5,6,9];

if 2 not in list:
    print('yes 2 is not in list');
elif 9 in list:
    print('yes 9 is in list');
else :
    print('non')    
#-----------------------------------------------------
# quiz
print("Please enter your age here", end=" ");
age = int(input());

if age<18:
    print('Sorry, you cannot drive')
elif age>18:
    print('Sure, you can drive')
else:
    print('you are exactly 18, So, we cannot decide your eligibilty to drive.')    