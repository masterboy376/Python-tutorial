# filePointer1 = open("text.txt", "a")# t is default

# numberOfCharacters = filePointer1.write("appended text\n");
# print(numberOfCharacters);

# filePointer1.close();

# --------------------------------------------------------------
# read and write/append
filePointer2 = open("text.txt", "r+");

# first read and then write
print(filePointer2.read())
filePointer2.write("thank you");

filePointer2.close()