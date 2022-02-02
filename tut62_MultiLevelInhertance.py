class Dad:
    programmer= True
    def isProgram(self):
        if(self.programmer):
            print(f'yes is program')
class Son(Dad):
    crypto= True
    def isCrtpto(self):
        if(self.crypto):
            print(f'yes is crypto')
class GrandSon(Son):
    crypto= 'metaverse'
    def isCrypto(self):
        print(f'yes i am metaverse')
derry = Dad()
jerry = Son()
merry = GrandSon()

derry.isProgram()
jerry.isProgram()
jerry.isCrypto()
merry.isProgram()
merry.isCrypto()