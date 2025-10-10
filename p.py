# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# print("Try programiz.pro")
s="500rose12lily43rose500rose12lily43rose500rose12lily43rose13tulip55gada87tulip"
d={}
ch=""
str=""
n=0
ns=""
k=""
for i in range(0,len(s)-1):
    ch=s[i]
    if(ch>="a" and ch<="z" and s[i+1]<="9"):
        str+=ch+" "
    else:
        str+=ch
str+=s[len(s)-1]+" "

for i in range(len(str)):
    if(str[i]<="9" and str[i]>="0"):
            ns+=str[i]
    elif(str[i]>="a" and str[i]<="z"):
       k+=str[i]
       
       
    else:
        n=int(ns)
        if(not d.get(k)):
                d[k]=n
                k=""
                n=0
                ns=""
        
        elif(d.get):
            n+=d.get(k)
            d.update({k:n})
            k=""
            n=0
            ns=""
        
    
print(d)
print(ns)
print(str)