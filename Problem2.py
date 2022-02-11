"""divide the apples 
Harry potter has got n number of apples. Harry has some students among whom, he wants to distribute the apples. These n number of apples are provided to harry by his friends and he can request for few more or few less apples
You need to print whether number in range mn to mx is a divisor of n or not"""

def appleDistribution(n,min,max):
    for i in range(min, max+1):
        if n%i==0:
            print(f'{i} is divisor of {n}')
        else:
            print(f'{i} is not the divisor of {n}')

while True:
    try:
        noOfApple = int(input('Enter the number of apples you have: '))
        min = int(input('Enter the minimum number of students: '))
        max = int(input('Enter the maximum number of students: '))
    except ValueError:
        print('Enter integerss only')
        continue
    if max<=min:
        print('This cannot be the range.')
        continue
    appleDistribution(noOfApple, min, max)
    userChoice = input('enter q to quit and any key to continue: ')
    if userChoice=='q':
        print('program ended!')
        break
    else:
        continue
