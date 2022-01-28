filePointer = open("text.txt", "rt"); # this will open the file

# this will empty the file pointer
#read
# print(filePointer.read());
# print(filePointer.read(10)); # will read 10 character
# print(filePointer.read(10)); # will read next 10 character
# for line in filePointer:
#     print(line, end="")


# read line
# print(filePointer.readline(), end='');
# print(filePointer.readline(), end='');


#read lines
print(filePointer.readlines())# eill return a list of lines


filePointer.close(); # this will close the file
