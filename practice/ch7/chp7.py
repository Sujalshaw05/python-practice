
#p1
n= int(input("enter the number"))

for i in range(1,11):
    print(i*n)


#p2
l=["sujal","shaw","prosenjit","shaw"]

for i in l:
    if(i.startswith("s")):
        print(f"hello {i}")


#p3
i =1
while(i<11):
    print(n*i)
    i+=1

#p4
for i in range(n):
    if(n%2==0):
        print("noy prime")
        break
else:
    print("prime")