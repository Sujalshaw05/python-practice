from typing import List,Tuple,Dict

# creatin list of int
num:List[int]=[1,2,3,4]

# creating tuples of a string and int
person:Tuple[str,int]=("alice",30,"sujal",21)

# dictionary of str key and int value 
score:Dict[str,int]={"sujal":15,"prosenjit":22}

print(num)
print(person)
print(score)
# walrus opretor 
if((n := len([1,2,3,4,5]))>3): # := -> this is called warlrus opretor , by this opretor we can reduce the code length . at the end the len of yhe list will be assigned to n
    print(f"the valu of {n} is greater than 3")
    


# specifing type 
n : int=5 # this statement is used to specify the type of the variable so that we can perform multiple opraton on that variable
def add(a:int,b:int)-> int: # so a:int , b:int this part spcifies that the function takes two integer as parameters & -> int this part specifies that the return type is also an int value  
    return a+b 


# match case
status =40
match status:
    case 200:
        print("ok")
    case 300:
        print("not bad")
    case 400: 
        print("better luck next time")
    case _:
        print("ubknown status ")

# merging dictionary

dic1={"a":1,"b":2}
dic2={"c":3,"d":4}
merged =dic1|dic2 # merging two dictionary  

print(merged)


# ecepyion hndling



try:
    a= int(input("enter a n umber"))
    print(f"your number is {a}")
#we can run different type of excepton block 
except ValueError as v:
    print(v) # it will run for value error 
except Exception as e :
    print(e) # it will run for exception 

print("thank you") # BECAUSE  we handling the exception the code will not crash and the nex lines of code will also be excuting


# eception raising 

a= int(input("enter a number"))
b= int(input("enter second  number"))

if(b==0):
    raise ZeroDivisionError("hey the opration can not be performed ") # we raise eror to notify the programmer abut the error and force full crash the program
else:
    print(a/b)

# finally key word

# finally is used inisde the function so if we apply finaly even if the function return from the function the finally block will be excuting 

def main():
    try:
        a= int(input("enter a number "))
        return
    except Exception as e:
        print(e)
        return
    #print("this will not be executing")   # yhis will not be excuting
    finally:
        print("inside the finally block") # but this will be excuting

main()