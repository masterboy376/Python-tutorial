"""

the next palindrome

you have to take the number from the user you have to find the next palindrom corresponding to that number.your first input should be the number of test cases and then tke all the test cases from the user.

"""

def nextPalindrome(no_of_testcases):
    inputs = []
    for i in range(0,no_of_testcases):
        try:
            inp = int(input(f"Enter the {i+1} number to find the palindrome of: "))
            inputs.append(inp)
        except ValueError:
            print('Please enter integer only')
            continue
    for item in inputs:
        fixedItem = item
        while True:
            if str(item) == str(item)[::-1]:
                print(f"the palindrome of {fixedItem} is {item}")
                break
            else:
                item+=1
                continue


nextPalindrome(2)