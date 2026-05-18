#as we know function is the part of code rthat we can use again again to promote data redundncy and repetaion
#def is the keyword use to define function

def add(x,y):
    return x+y
print(add(2,3))

#thre are two functions types first Built-in and second user defined 
#1.Built.in
l=[1,2,3,4,5,6,7,8,9]
p=["a","b","c","d","e","f","g","h"]
print(len(l))
print(max(l))
print(min(l))
print(round(6.22))

class a:
    pass
class b(a):
    pass
print(issubclass(b,a))

print(sum(l))

print(sorted(l))
print(zip(l,p))
print(pow(1,2))

a =  int(3.4)
print(a)
print(type(a))

a = '10.7'
print(type(float(a)))


x = ["a","b","c"]
y = [10,20,30]
for i,v in enumerate(x):
    print(i,v)

l=zip(x,y)
print(list(l))

print(dict(l))

print(tuple(l))

x ='python'
a=hash(x)
print(a)

print(int("10"))

l=[]
print(bool("'False"))
print(bool(0))
print(bool(l))


x = [3,1,2]
l=[90,12,31,1]
print(sorted(x))
print(x)
print(l.sort())
print(l)

for i in range(65,91):
    print(chr(i))

for i in range(92,123):
    print(chr(i))

for i in range(123,130):
    print(chr(i))

print(ord('A'))

print(bin(10))
print(hex(10))
print(oct(10))

print(hex(4))
print(oct(4))

print(hex(21))
print(oct(10))

print(hex(26))
print(oct(26))

print(hash(True))
print(hash(1))

def test():
    print(5)

x = test()

print(x)