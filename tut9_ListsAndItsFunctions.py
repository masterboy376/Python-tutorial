grocery = ['sugar', 'salt' , 'bread' , 'hajmola', 'bike fuel' , True,13 ,{}];
print(grocery);
print(grocery[3]);

numbers=[1000,343,434,-5,-4.99999,46,6,4,463];
print(numbers)
numbers.sort();# You can not asign or print this syntax directly
print(numbers)
numbers.reverse();# You can not asign or print this syntax directly
print(numbers)

# list slicing
print(numbers[0:4]);
print(numbers[::2]);
print(numbers[::-2]);# will work
print(numbers[1:4:-2]);# will not work

print(len(numbers));
print(max(numbers));
print(min(numbers));

#changing list
numbers.append(7);#add at end
print(numbers);
numbers.insert(1,12314);# add in the middle
print(numbers);
numbers.remove(7);# removes 7 from the list
print(numbers);
numbers.pop(0);# remove 0th index
print(numbers);
numbers.pop();# remove from last
print(numbers);

#=========================================================
# list - mutable
# tuple - immutable
#=========================================================
lst = [1,2,3]; # list
tp = (1,2,3); # tuple

#lst[1] = 2000;#possible
#tp[1] = 2000;#Impossible

# note : a tuple of onw item should be like (1,) and not like (1) 
#---------------------------------------------------------
#how to swap two numbers
a=1;
b=2;
print('a:', a)
print('b:', b)
# traditional

# temp = a;
# a = b;
# b = temp;

# in python

a,b = b,a;

print('a:', a)
print('b:', b)

