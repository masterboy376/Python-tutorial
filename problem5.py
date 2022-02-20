"""
take list as input and return a palindromed list
"""

def nextPalindromeList(lst):
    try:
        newLst = []
        for item in lst:
            if type(item) is int:
                while True:
                    if str(item) == str(item)[::-1]:
                        newLst.append(item)
                        break
                    else:
                        item+=1
                        continue
            else:
                print('please give list of integer as input')
                return
        print('the new palindromed list is ')
        return newLst
    except Exception:
        print ('please give list of integer as input')


print(nextPalindromeList([1,5,346,3463,34,67,2,8]))