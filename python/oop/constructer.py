#constructer is a special function of a class which automatically initilize and operate  at the time of object creation
# __init__ is a constructer
#Constructer process has two part of 1. __new__() function which allocate memory to the object and __init__() function initialize the attributes and the methods of a class

class bank:
    def __init__(self,name,acc):
        self.name = name
        self.acc=acc

    def dis(self):
        print(" Name : ",self.name, " Accont number : ", self.acc )

b = bank("Punit",1234)
print(b.dis())

b.name = "Pratham"   #later we can change the attributes
print(b.dis())


# there two types of parameters 1.Paramatrized 2. Default

# Defult constructer is a constructer without any parameter

class animal :
    def __init__(self):
        self.name = "Wolf"
        self.id= "W01"
    def dis(self):
        print("Aniaml : ",self.name," Animal ID : ",self.id)

a = animal()
a.dis() 

# parameter is as given in bank class