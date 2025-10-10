 # file i/o


# file read
f=open("./s.txt")# used to open it
data=f.read()# used to read the file
print(data)
f.close()# after performing the opration you have to close the file



# reding file via with statement
with open("s.txt") as a:
    print(a.read())





# file write 
st ="hey it's a new file " 
g=open("n.tet","w")# if the file does not exists it will create it


g.write(st)# use to write in the file

g.close()# used to close the file



# printing the file lines 

p=open("l.txt")
# k=p.readlines()# this returns list of tose lines
# print(k)

j=p.readline()# this returns a single line 
print(j)
p.close()