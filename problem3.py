# food and calories
# you visit a retaurent named eat and chill and food item in the retaurant are sorted based on the amount of calories . you have to reverse this list of food items and their calories.
# you have to use three methods to reverse the list 
# 1. inbuilt method of python 
# 2. listname[::-1] slicing trick
# 3.swapping first element with last one and second element with second last one.
# then check whether these three methods returns the same list or not.

class reverseList:
    @staticmethod
    def builtinReverse(lst): # note:-this will reverse the actual list 
        lst.reverse()
        return lst
    @staticmethod
    def slicingReverse(lst):
        new_lst = lst[::-1]
        return new_lst
    @staticmethod
    def customReverse(lst):
        lengthOfList = len(lst)
        if lengthOfList%2==0 :
            finalIndex = lengthOfList-1
            for initialIndex in range(0,(lengthOfList/2).__round__()):
                lst[initialIndex], lst[finalIndex] = lst[finalIndex], lst[initialIndex]
                finalIndex-=1
                return lst
        else:
            finalIndex = lengthOfList-1
            for initialIndex in range(0,(lengthOfList-1/2).__round__()):
                lst[initialIndex], lst[finalIndex] = lst[finalIndex], lst[initialIndex]
                finalIndex-=1
                return lst
    @staticmethod
    def iteratableReverse(lst):
        new_list = [element for element in (reversed(lst))] # reversed function returns a list iterator
        return new_list

    
myList = ['roti', 'rice', 'panchamrit', 'halwa', 'gujiya with jelabi']
print(reverseList.customReverse(myList))