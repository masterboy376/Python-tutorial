class Employeee:
    #assume that name and email is connected
    def __init__(self , fname , lname,):
        self.fname = fname 
        self.lname = lname

    def explain(self):
        return f"This is {self.fname} {self.lname}"

    @property#convert the function into a property ----> this will create a atribute with no error
    def email(self):
        if self.fname==None or self.lname ==None:
            return None
        return f"the email is {self.fname}.{self.lname}@.com"

    @email.setter # will set the email
    def email(self, string):
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]
        
    @email.deleter #will delete the email
    def email(self):
        self.fname = None 
        self.lname = None 
        
        
sam = Employeee("Sambhav" , "Kaushik")
# kath = Employeee("Katherine" , "Langford")

print(sam.email)
print(sam.fname)
print(sam.lname)


sam.email="sambhav.kaushik@.com"

print(sam.email)
print(sam.fname)
print(sam.lname)

del sam.email

print(sam.email)
print(sam.fname)
print(sam.lname)