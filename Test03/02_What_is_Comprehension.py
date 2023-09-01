#2.	What is Comprehension.
#comprehnsin it will give sort and cansis way to create new sequnces such as:(list,set,dict,etc) using previusly defined sequnce.
#there are 4 types of comprehensios
#01:list comprehension
#02:dict comprehension
#03:set comprehension
#04: generator comprehension

#. example

# filtering even number in given list using list comrehnsion

list = [1,8,7,2,3,4]

comp= [var for var in list if var % 2==0]
print(comp)
x1 = [ ]
list = [1,8,9,5,4,6,3]
com = [x1.append(var*2) for var in list if var % 2==0]
print(x1)

# filring odd number with qube using dict comprension
list =[1,8,7,5,9,6,4,3]
comp = {var:var**3 for var in list if var % 2 !=0}
print(comp) 
#maping using dict comprension
name  =["raj","ram","lax"]
age = [28,26,23]
comp = {key:value for key, value in zip(name,age)}
print(comp)

