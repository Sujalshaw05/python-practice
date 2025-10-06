# dictonary is just a list of key value pair where we can store values with asociated keys
d={}# an empty dictionary
marks={
    "sujal":100,
    "prosenjt":95,
    "shaw":23
}
print(marks,type(marks))
print(marks.items())# returns dicenory items in key value pairs
print(marks.keys())# returns only keys of the dicnary
print(marks.values())# returns only values 
marks.update({"sujal":55,"rohan":77})# updates the values if the key exists or it will add that key and value

print(marks)


# -- set --
# properties
# 1.   set does not contains duplicates
# 2. sets are unordered
# 3. we can not change set items
# 4.  we can not acces them by index es


s={}# this is an empty dictionary

s1=set()# this is a empty set

s2={1,2,3,4,"sujal"}# this is a set
s2.add(344)
print(s2)
s2.remove(2)# removes specific element
print(s2)
s2.pop()# removes random value
print(s2)
s2.clear()# clears the whole set 
print(s2)

s3={1,2,3,4,4}
s4={5,6,7,8,1}
print(s3.union(s4))# combines all uniqe vlues from two sets
print(s3.intersection(s4))# takes only common value