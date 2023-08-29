#01: what is class:
# class is a blueprint of object it has list of variables,data and funtion or methods.

class clac:

    def add(x1,y):
        x = x1+y
        return x
    def sub(x1,y):
        y = x1-y
        return y
    def mul(x1,y):
        z = x1*y
        return z

while True:
 print("01:add,02:sub,03:mul")
 x2 = int(input("select any one"))
 x1 = int(input("enter the number:"))
 y = int(input("enter the number:"))

 if x2 ==1:
    print(clac.add(x1,y))
 elif x2==2:
    print(clac.sub(x1,y))  
 elif x2==3:
    print(clac.mul(x1,y))



