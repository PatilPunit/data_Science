#lis is dzta structure used tos tore hetrogeneous data
import math
p=math.pow(2,3)
l=[1,2,3,"punit",True,3.14,p] 
print(l)

# its 0 based indexing
print(l[0])
print(l[1:4])

#list support negative indexing
print(l[-1])
print(l[-3:-1])

#lists are mutable or changable
# we can modify existing list without making new one
l[1]=10
print(l)

#there are methods to work with list
lw=[1,2,3,4,5,6,7,8,9]
print(lw.pop()) #returns last elemnt
lw.append(19)
print(lw) # to add element in last
lw.remove(2)
print(lw)
lw.clear()
print(lw)
c= l.count(10)
print(c)
#repetation

r=l*3
print(r)

#nested listing
l =[[1,2,3,4],[6,7,8,9]]
for i in l :
    print(i)

print(l[1][3])

l=[1,2,56,21,54,91,0,8]
print(l[::1])

print(l.sort())
print(l)
a=[10]
b=[10]
print(b is a)
print(b==a)