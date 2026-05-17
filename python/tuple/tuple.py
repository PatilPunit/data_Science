#biggest diffrence in list and python is that tuple is immutable

t=(1,2,3,4,5,6)
print(type(t))
#tuple is unchangable we alaways need to make new tuple 
#t[0]=2

#methods
no=t.count(1) # the number of lements in tuple
print(no)

#concetanation

t=(1,2,3)
t2=(4,5,6)
tp=t+t2 
print(tp)

#repetation

r=t*3
print(r)

#membership

print(1 in t)

# tuple packing
x =1,2,3
print(x)
print(type(x))

# tuple unpacking
a,b,c=1,2,3
print(a)

