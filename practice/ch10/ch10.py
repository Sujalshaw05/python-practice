class emp:
    name="sujal"
    salry=12000

    def info(self): # this is just a function of the class . we have to pass a object to the function
        print(f"name is {self.name} and salary is {self.salry}")

    def __init__(self): # this is the constructor of the class & this the default constructor
        print("constructor called")
    def __init__(self,name ,salry): # this is the constructor of the class & this is the parameterized constructor
        self.name=name
        self.salry=salry
        print("constructor called")

    @staticmethod
    def greet():# in case of static method we don't have to pass any object & and this belongs to the class itself 
        print("hello how are you")

    

s=emp("sujal shaw ",50000)
p=emp("prosenjit shaw ",34000)
s.name="prosenjit shaw" # this is called instance attribute it will over ride 
s.info()
s.greet()
p.info()
p.greet()