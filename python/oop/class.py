#class is blueprint to create objects
# class contain data andd methods o operate on
#objects are the instance of a class can acces the class methodas and attributes

class  animal:
    def get(self):
        self.a = input("enter the animal : ")

    def dis(self):
        print("Aniaml name : ", self.a)
a = animal()

a.get()
a.dis()