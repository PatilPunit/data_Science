#exception is a error in python
#every exception need to be treated profesionly with proper exception handling block

try:
    age=int(input("enter : "))
    if age > 18 : 
         print("valid ")
    else:
        print("invalid")

except ValueError :
    print("enterd valuye is wrong")

#in this block a try checks for the code that can occured error in this case a  invalid input can cause error
#Valueerror is  a exception block to handle that error

try :
    a = 10
    a/0
except ZeroDivisionError:
    print("Cant divide")
else:
    print("0")

#finally is the conditon whre the statemnt under finally will always happend

try:
    age=int(input("enter : "))
    if age > 18 : 
         print("valid ")
    else:
        print("invalid")

except ValueError :
    print("enterd valuye is wrong")
finally :
    print("at the end value should be valid")

#to coustmize own exceptions
class horseError(Exception):
    def __init__(self, e):
       self.e = e


try :
    age = 91
    if age < 100:
        raise horseError("Horse is eating  grass")

except horseError as e:
    print("error :",e)