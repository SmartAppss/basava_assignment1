#5.	Create a program that generates a random number 
import random
list = [1,2,3,4,5,6,7,8,9]

print(random.sample(list,5))
#------------------------------------
x = (1,2,3,4,5,6,7,8,9)
y = (7,8,9,4,5,6,1,2,3)
x,y=y,x
z = (x+y)
print(z)
