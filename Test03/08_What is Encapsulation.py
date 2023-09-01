#what is encapsulation
#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

class base:
    def __init__(self):
        self.a = "ram"
        self.c = "raj" #protected number this can be acess from parent class into child class 
        self._d="tan"  # private number this can not acess from parent class into child class
      
class child(base):

    def __init__(self):
        base.__init__(self)
                
obj1 = child()
print(obj1.a)
print(obj1._d) 
#print(obj1.__d) 
#print(obj1.c)      

#Private members
#Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, 
#there is no existence of Private instance variables that cannot be accessed except inside a class.

#However, to define a private member prefix the member name with double underscore “__”.