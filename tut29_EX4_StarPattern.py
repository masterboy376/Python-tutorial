def starPattern1(n):
    i = 0;
    while(i<=n):
        print('@'*i);
        i += 1;

starPattern1(10); 

# or 

def starPattern2(n):
    for i in range(1,n+1):
        print('@'*i);
        

starPattern2(10);  