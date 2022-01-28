f = open('text.txt','r+');

print(f.tell())# tell-----> will tell the position of the file pointer in terms of characters
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.seek(0))# seek-----> will take the file pointer back to the character position we have given
print(f.tell())
print(f.readline())


f.close();