import random

computerInt = random.randint(1,4)

if(computerInt == 1):
    computerChoice = 'g'
elif(computerInt == 2):
    computerChoice = 's'
if(computerInt == 3):
    computerChoice = 'w'

userChoice = input('snake-s, water-w, gun-g ');

if (userChoice=='s' and computerChoice=='g') or (userChoice=='g' and computerChoice=='w') or (userChoice=='w' and computerChoice=='s'):
    print(f'oops! you lost. computer choose {computerChoice}')
elif (userChoice=='g' and computerChoice=='s') or (userChoice=='w' and computerChoice=='g') or (userChoice=='s' and computerChoice=='w'):
    print(f'congo! you won. computer choose {computerChoice}')
elif (userChoice=='g' and computerChoice=='g') or (userChoice=='w' and computerChoice=='w') or (userChoice=='s' and computerChoice=='s'):
    print(f'tie! you draw. computer choose {computerChoice}')