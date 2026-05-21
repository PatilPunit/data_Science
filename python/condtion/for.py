# while True:
#     print("Infinite")

x = 1

while x <= 3:
    print(x)
    x += 1



x = 0

while x < 5:
    x += 1

#     if x == 2:
#         continue

#     print(x)

# x = 1

# while x < 10:
#     print(x)

print(2 ** 3 ** 2)

x = [1,2]
y = x

print(x is y)

x = 0

while x < 3:
    print(x)
    x += 1
x = [1,2,3]
x.append([4,5])

print(len(x))
x = [[]] * 3

x[0].append(1)

print(x)

a = (1, 2, [3,4])

a[2].append(5)

print(a)

x = {1,2,3}

print(x.pop())

def test(x=[]):
    x.append(1)
    return x

print(test())
print(test())

print(0.1 + 0.2 == 0.3)

a = [1,2,3]

print(a[::-1])

print([i*i for i in range(3)])

a = "abc"

print(a * 3)

x = [1,2,3]

print(x == x.copy())
print(x is x.copy())

x = [1,3,4,5,6,7,9,0,10]

for i in x:
    x.remove(i)

print(x)

def func(a, b=[]):
    b.append(a)
    return b
import sys as s
print(func(1))
print(func(2))
print(func(3, []))
s.exit()
import  os
import random as rd

l = [1,2,3,4,5]
print(type(rd.shuffle(l)))
