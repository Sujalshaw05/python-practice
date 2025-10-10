class emp:
    name="sujal"
    salry=12000
    def info(self):
        print(f"name is {self.name} salary is {self.salry}")

class coder:
    language="python"
    def lan(self):
        print(f"the language {self.language}")
# inheritance
class program(emp,coder): # this is called multiple  inheritance because we are inheriting a multiple  classes in a class  
    pass
class person(emp): # this is called single   inheritance because we are inheriting a single class
    def __init__(self):
        
        super().__init__() # super function is used to call parent constructor or used in passing values to parent class
    

p=program()
p.info()
p.lan()


# multi level in heritance 

class stu(person): #  this is called multi level inheritance because wr are inheriting propertis from emo->person->stu 
    pass

s= stu()


class gg:
    h=1
    @classmethod
    def show(cls):
        print(f"we are printin the class atribute {cls.h}")

d=gg()
d.h=55 # this will not over ride the class attribute 
d.show()  