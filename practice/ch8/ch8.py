# function without parametrs

def goodday():
    print("hello")


goodday()

# function with parameters

def greet(name):
    print("hello , "+name)

greet("sujal")

# function with return value

def re():
    return 5

print(re())

# function with default parameters

def de(name,gre="thank you"):
    print("hello ,"+name)
    print(gre)

de("sujal")# in default parameters if we dont pass the value it will use it's default value 
de("sujal","thanks")# if we pass the value for default parameters then it will over ride the value of default parameters


# recursion    

def fac(n):
    if(n==1 or n==0):
        return 1
    return fac(n-1)*n

print(fac(6))


# how to prevent print function to print on a new line

print("a")
print("b")
print("c", end="")# this will print c & d in same line but not other following line
print("d",)