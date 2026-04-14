# inheritence is a mechanism to transfer properties of one class to another class
# 1. Single inheritnce
# 2. Multiple inheritnce
# 3. Multilevel Inheritence

class grand:
    def g():
        print(" Hi i am grand parent class") 
class child(grand):       # single inheritence
    def c():
        print(" Hi i am child class")
c = child
c.g()
c.c()

class grandChild(child):  # multilevel inheritence 
    def gc():
        print(" here is multilvel inheritence i contain properties of grand and child")

gc = grandChild
gc.g()
gc.c()
gc.gc()
class child(grandChild,child,grand): #multiple inheritence
    def ch():
        print("here is a multiple inheritence i  contain multiple class's properties ")
ch = child
ch.g()
ch.c()
ch.gc()
ch.ch()

# in multiple inheritence there should be MRO porder means down to up order

# for callinng constructer of parent class there is function used called super()=

class animal:
    def __init__(self):
       self.name = "Wolf"
       print(self.name)

class child(animal):
    def __init__(self):
        super().__init__()
a = animal()

