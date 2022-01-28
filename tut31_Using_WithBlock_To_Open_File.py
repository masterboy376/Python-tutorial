with open('text.txt','rt') as f:
    a=f.read()
    print(a)

# or 

f= open('text.txt','rt')
b=f.read()
print(b)
f.close()
