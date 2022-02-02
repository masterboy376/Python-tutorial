class Employeee:
    def __init__(self , fname , lname,):
        self.fname = fname 
        self.lname = lname

    def explain(self):
        return f"This is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname ==None:
            return None
        return f"the email is {self.fname}.{self.lname}@.com"

    @email.setter
    def email(self, string):
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]
        
    @email.deleter
    def email(self):
        self.fname = None 
        self.lname = None 
        
        
sam = Employeee("Sambhav" , "Kaushik")

#object introspection
print(type(sam))
print(id(sam))
print(dir(sam))# will give all the functions that can be performed with sam
print(type(sam.email))

import inspect
# print(inspect.getmembers(sam))

#quiz
dic={
    "classMembers":inspect.getmembers(sam)
}
print(dic)