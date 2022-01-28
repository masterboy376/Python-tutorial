from json.tool import main


def funcGreet(str):
    print(str)

print('the name is',__name__)
if __name__=='__main__': # this is because if we run this func in any other file then code below this will not execute    
    funcGreet('hihihihi')    
