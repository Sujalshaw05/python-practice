#lists are like arrays in javascript where we can store different types of data in a single list
a=["sujal",2,3,"shaw"]
print(a)
print(a[0])
a[0]="prosenjit"
print(a[0])
print(a[1:4])# list slicing like string

# list methods will change the orignal list

a.append("hi how are you")# adds the string at the end
print(a)
b=[7,5,64,3,2,1]
b.sort()# used to sort the list in accending order
print(b)
b.reverse()# used to reverse the list
print(b)
b.insert(2,45)# used to insert a value at any position
print(b)
b.pop(3)# used to pop a value from any position
print(b)

print(b)

# tupples are like list where we can store different types of data but we can not change the values of the tuples

c=(1,2,3,"sujal",False,4,5,6)
print(type(c))
print(c.count(2))# returns the frquency of the element
print(c.index(3))# returns the index of the element
