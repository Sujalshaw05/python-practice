import numpy as np

# this is not efficent
l=[1,2,3,4,5]
a=0
for i in l:
    a+=i
a=a/len(l)

# this is efficent
b= np.array([1,2,3,4,5])# creating array forma list so that we can perform various oprations . numpy is 50-100 time faster than normal python  

z=np.zeros(3) # creating array with zeros for 1D array
o=np.ones((2,3)) # creating array with ones for 2D array
r=np.full((2,2),7)# creating 2D array with value 7 .(2,2) -> it defines the size of the array
arr=np.arange(1,10,2)# ARANGE FUNCTION RETURNS A LIST , 1-> starting value.10-> ending value. 2-> step size
i=np.eye(4)# creating identity matrix

print(a)
print(np.mean(b))
print(z)
print(o)
print(r)
print(arr)
print(i)


# information about the array
n1=np.array([[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]])
n2=np.array([
    [1,2,3],
    [3,4,5]

])
n3=np.array((
    [1,2,3]
))
print(n1.ndim)# prints the dimention of the array
print(n2.ndim)
print(n3.ndim)


print(n1.shape)# prints the shape of the array
print(n2.shape)
print(n3.shape)
print(o.shape)# returns the shape of the array mans no of row & colum
print(o.size)# returns the total no of elements present in a array


print(n1.dtype)# prints the data type present in the array

n1=n1.astype(float)# converting the typ we can not per form int(n1) because it's array
print(n1.dtype)

print(n1*2) # numpy automatcaly ferforms opration on individual element 




# agrigation functions 

print(np.sum(n1)) # used to sum all elements
print(np.mean(n1))# used to find mean of all element
print(np.min(n1))# used to find the min value in the array
print(np.max(n1))# used to find max value in the array
print(np.std(n1))# used to find std
print(np.var(n1))# used to find var

