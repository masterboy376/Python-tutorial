from msilib.schema import PublishComponent


# Public(all classes and objects):- by default
# Protected(isude the class and its child classes):- _
# Private(inside the class):- __ 

class Dad:
    programmer= True
    __verse= 'metaverse'
    _crypto= True
class Son(Dad):
    pass


derry = Dad()
jerry = Son()

print(Dad.programmer)
# print(Dad.__verse)
print(Dad._crypto)
print(jerry._crypto)
print(derry.programmer)
# print(derry.__verse)
# print(derry._crypto)

print(derry._Dad__verse)#name mambling


