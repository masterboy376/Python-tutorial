"""
take two number a and b as the input and generate a random number between these. and give player 1 the chances and player 2 the chances to play and guess the number and at the end release the winner on the bases of the lesser no of chances taken.
"""

def ran_num(a,b):
    import random
    number = random.randint(a,b)
    return number

if __name__ == "__main__":
    mn = int(input('Enter the minimum number of a range\n'))
    mx = int(input('Enter the maximum number of a range\n'))

    number = ran_num(mn,mx)
    numberOfGuesses_player1 = 0
    while(True):
        numberOfGuesses_player1 +=1
        inp = int(input('Player 1 Guess the number '))
        if(inp>number):
            print('your input is greater than the actual number')
            continue;
        elif(inp<number):
            print('your input is less than the actual number')
            continue
        elif(inp==number):
            print('you guessed it right the number was',number)
            break    

    
    number = ran_num(mn,mx)
    numberOfGuesses_player2 = 0
    while(True):
        numberOfGuesses_player2 +=1
        inp = int(input('Player 2 Guess the number '))
        if(inp>number):
            print('your input is greater than the actual number')
            continue;
        elif(inp<number):
            print('your input is less than the actual number')
            continue
        elif(inp==number):
            print('you guessed it right the number was',number)
            break    

    if (numberOfGuesses_player1>numberOfGuesses_player2):
        print('player 2 won!')     
    elif (numberOfGuesses_player1<numberOfGuesses_player2):
        print('player 1 won!')     
    else:
        print('draw!')     
    

