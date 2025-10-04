name ="sujal"#this is a string . strings are immutable .
nameshort=name[0:3]#it will return suj== 0,1,2 index of name
ch=name[1]#this will return a single charecter
print(ch)
print(nameshort)
print(name[:3])#this will return suj. first place is empty means 0 
print(name[1:])#this will return ujal. last place is empty means len-1
print(len(name))# for printing the length 

print(name[-4:-1])#this will return ujal . -1= last charecter -4=4th charecter from lastindex
a="12345678910"
print(a[1::2])# this wull print 24681 1= start from index 1 , go till last index &  skip 2 indeces
print(name.endswith("al"))# return's true if the string ends with al
print(name.startswith("su"))# return's true if the string starts with su
print(name.capitalize())# convert's the string into capitalize string
b="this is the new new book"
print(b.replace("new","old"))# replaces all ocurences of new with old


