"""
Rohan das is a fraud
rohan das is a fraud by the nature. rohan das has wrote a python function to print a multiplecation table of a given number and put on of the values randomly generated as wrong.
rohan das did this to fool his classmates and make them commit a mistake in a test. you cannot tolerate this! so you decided to use your python skills to counter Rohan's action by writing a python program that vlaidates rohan's table.
your function should be able to find out the wrong values in rohan's table and expose rohan das as a fraud.
rohan's table returns a list.
"""
from operator import index
from random import randint


def rohanTable(n):
    try:
        import random
        numToInsert = randint(n,n*10)
        indexToInsert = randint(1,11)
        table = []
        for i in range(1,11):
            if indexToInsert == i :
                table.append(numToInsert)
            else:
                table.append(i*n)
        return table
    except ValueError:
        return 'please enter a integer'


def samValidator(lst):
    try:
        print(lst)
        for i in range(1,11):
            if lst[i-1]==lst[0]*i:
                continue
            else:
                return f'the value a the index {i-1} is wrong'
        return None
    except ValueError:
        return 'please enter a integer'
    except TypeError:
        return 'please enter a list'


if __name__=='__main__':
    print(samValidator(rohanTable(6567)))