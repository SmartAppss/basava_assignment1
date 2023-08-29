#what is encapsulation
#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

class base:
    def __init__(self):
        self.a = "ram"
        self._c = "raj"
        self.d="tan"
      
class child(base):

    def __init__(self):
        base.__init__(self)
                
obj1 = child()
print(obj1.a)
print(obj1._c) 
print(obj1.d) 
#print(obj1._c)      