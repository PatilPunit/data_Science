#dictionary is the collection of key and value pairs

student={
    "name" :"Punit",
    "age":17,
    "marks":99
} 
studentq={
    "name" :"Pratham",
    "age":15,
    "marks":101
} 

print(student)

#we can access kay and valus by

print(student.keys())
print(student.items())
print(student.values())

#we can change value of dictionary but cant a key basicaaly a key isnt mutable

student["age"]=20
print(student["age"])
student.update({"age":30})
student.update({"place":"pune"}) #even the kay and value not in dict get added
print(student)

#to cpoy dict
stud = student.copy()
print(stud)

#to give the dict
studw = student
print(studw)   #by copy we just copy the value but byt this we are giving memory of that dictionary

# to delete data
print(studw.pop("name")) # only deletes the value
print(studw)

del studw['age'] # delete value and key
print(studw)


dic = {1:'a',2:'b',3:'c',4:'d'}

print(dic.values())
print(dic.items())
print(dic.keys())

for i in dic:
    print(i)

for i in dic.values():
    print(i)

for i in dic.keys():
    print(i)

for i,j in dic.items():
    print(i,j)

dic.update({(1,2):'tuple',frozenset((1,2)):'fz'})
# dic.update({[1,2]:'list'})


student = {
    "name": "Jarad",
    "marks": {
        "math": 90,
        "python": 95
    }
}

print(student.get('marks','python'))