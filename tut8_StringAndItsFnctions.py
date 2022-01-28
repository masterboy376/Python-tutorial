myStr ="sam is a good boy go "
print(len(myStr));
# string slicing
print(myStr[2]);
print(myStr[0:3]);# slicing of a string (0->including, 3->excluding)
print(myStr[0:1000]);# slicing of a string (full sting)
print(myStr[0:17:2]);# this kind of slicing will slice the string by skipping one character
print(myStr[::]);
print(myStr[0::2]);
print(myStr[:17:2]);
print(myStr[0::1000]);
print(myStr[-4:-1]);# from left side
print(myStr[::-1]);# reverse the string
print(myStr[::-2]);# reverse the string and then skip 1 charcter

# string functions
print(myStr.isalnum());# true for 'samkaush' | false for 'sam kaush'
print(myStr.isalpha());# true for 'samkaush' | false for 'sam kaush'
print(myStr.endswith('boy'));
print(myStr.count('o'));# counts the occurance of the given sub string
print(myStr.capitalize());# capitalizes the forst letter
print(myStr.find('go'));
print(myStr.find('go'));
print(myStr.lower());
print(myStr.upper());
print(myStr.replace(' go ', ' hahah '))

