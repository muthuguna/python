import math
n = 8
fac = 1
dic = {}
for i in range(1,n+1):
    dic[i] = i*i
    if(n==1):
        break
    fac = fac*i
    if(i==n):
        print(fac,end="\n")
    else:
        print(fac,end=", ")
print(dic)

inpt = "345,678,559,331,124,985"
lst = inpt.split(",")
print(lst)
print(type(dic))
print((tuple(lst)))

inpt1 = "100,150,180"
c=50
h=30
for x in inpt1.split(","):
    print(round(math.sqrt((2*c*int(x))/h)), end=", ")
