#set is a collection of dat where dat cant be repeated

s={1,2,3,4,5,6,7,8} #basic set

#the empty dictonary is like
d={}
#and empty set be like
e=set()

print(s)
# as i mentioned set cant take repetative data

sw={1,2,3,4,4,1,5,6,8,8,8}
print(sw)

#set is unorderd so basically we cant index the set
# print(sw[1])

#methods
s.add(566)
print(s)
s.clear()
print(s)

#we can use opeartions such as diffrence ,inetrsection and symmetric diffrence etc.

s={1,2,3,4,5,6,7,8,9}
sw={1,2,60.32,67,8,9}

print(s.difference(sw))
print(s-sw)

print(s.intersection(sw))
print(s&sw)

print(s.symmetric_difference(sw))
print(s^sw)

print(s.union(sw))

#superset and subset

sub={1,2,3,4}
sup={1,2,3,4,5,6,7,8}
print(sup.issubset(sub))
print(sup.issuperset(sub))

x = {1,2,3}
x.add((4,5))

print(x)


a = (1,2)
b = (1,2,3)

print(a < b)

dic={10:'a',20:'b'}
x.update(dic)
print(x)

x = {1, True, 1.0}

print(x)