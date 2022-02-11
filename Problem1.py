# your age in 2090 
# tke year of birth or age form the user and tell them when they will be 100 years old. Thwy can then optionally provide a year and your program must tell their age in thetnparticular year.
# youshould be handeling all sorts of error :
# 1. you are not yet born 
# 2. you seems to be the aldest people alive 
# 3. ay other error as well 

class Age:
    def __init__(self, userInput):
        if type(userInput) is not int:
            raise Exception('Input should be integer.')
        elif userInput>=136 and userInput<1922:
            raise Exception('You seems to be the oldest person to alive')
        else:
            self.userInput=userInput

    def getYearOfCentury(self):
        if self.userInput>=1922:
            return f'You will be 100 years old in the year {self.userInput+100}'
        else:
            return f'you will be 100 years old in the year {2022+(100-self.userInput)}'

    def getAge(self,year):
        if self.userInput>=1922:
            return f'You will be {year-self.userInput} years old in the year {year}'
        else:
            return f'You will be {(year-2022)+self.userInput} years old in the year {year}'


while(True):
    userInput = int(input('Enter your Age or Year of birth: '))
    print('Enter your choice:')
    print('1. year of century')
    print('2. get age in random year')
    userChoice = int(input())
    age = Age(userInput)
    if userChoice==1:
        print(age.getYearOfCentury())
    elif userChoice==2:
        year = int(input('Enter the year in which you want to find your age: '))
        print(age.getAge(year))
    else:
        print('Pleare enter the valid input')
        continue
    finalInput = input('enter q to quit and any key to continue')
    if finalInput=='q':
        break
    else:
        continue
# age = Age(2004)
# print(age.getYearOfCentury())
# print(age.getAge(2050))