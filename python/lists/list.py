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
#repetation

r=l*3
print(r)

print(l[-3:-1])
print(l[1:3])

print(l)
print(l[1:3])
print(l[-4:-2])

i=l.index(10)
print(i)
l.remove(3.14)
print(l)