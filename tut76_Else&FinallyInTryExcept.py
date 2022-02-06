f1 = open('text.txt')
try:
    f = open("doesnotexist.txt")
    # f = open("text.txt")
except EOFError as e:
    print('EOFError ocurred',e)
except IOError as e:
    print('IOError ocurred',e)
except Exception as e:
    print('Exception ocurred',e)
else:# this will run only if except didn't ran
    print('i am else')
finally:# this will run anyway
    print('i am finally')
    f1.close()
    # f.close()

print('imp1')