import random
from tkinter import BROWSE;
number = random.randint(0,100);

numberOfGuesses = 10

while(True):
    if(numberOfGuesses>0):
        numberOfGuesses -=1
        print('Guess the number', end=' ');
        inp = int(input());
        if(inp>number):
            print('your input is greater than the actual number')
            continue;
        elif(inp<number):
            print('your input is less than the actual number')
            continue;
        elif(inp==number):
            print('you guessed it right the number was',number);
            break;   
    else:
            print('Game Over, you have used all your chances');
            break;           

