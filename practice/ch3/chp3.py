a=input("enter your name")#used to take inputs from the users
print(f"hello my name is {a}")# used to add variables in a string easily
letter='''dera <|name|>
you are selected 
<|date|>
'''
print(letter.replace("<|name|>","sujal").replace("<|date|>","12/01/1026"))#this is called method chaining

n="hi  my  name  is  sujal  "#this is used to find the first occurance of "  " if not find it return's -1
print(n.find("  "))