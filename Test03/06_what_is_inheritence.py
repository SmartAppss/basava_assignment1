#06:what is inheritence
# Inheritance is the capability of one class to derive or inherit the properties from another class. 

class first:
    def x(self):
        print("main class")

class second(first):    
    def y(self):
        print("child class")

class third(second):
    def z(self):
        print("sub class")


A=first()
#A.x()
B = second()
#B.y()
C = third()
C.z()
C.y()
C.x()



