i = 0;

while(True):
    if (i<10):
        i=i+1;
        # will not run the below code in i<10 re-execute loop without running the below continue
        continue;
    print(i)
    if (i==45):
        #exit the loop
        break
    i=i+1;

print(i)

# quiz
while(True):
    inp = int(input());
    if(inp<100):
        continue;
    else:
        print('congratulations, the input is greater than 99');
        break;    