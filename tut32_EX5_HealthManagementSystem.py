from xml.etree.ElementTree import tostring


def getDate():
    import datetime 
    return datetime.datetime.now()

def getYourHealth(name, need, date):
    file = 'EX5/'+name+'_'+need+'.txt'
    with open(file,'rt') as f:
        a= f.read()
        print('['+date+']')
        print(a)
    

name = input('Your name here ')
need = input('Your need here ')
date = str(getDate());

getYourHealth(name, need, date)
# print(date)