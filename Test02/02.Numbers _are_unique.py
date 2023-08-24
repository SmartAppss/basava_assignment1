#2.	WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.
"""x  = [120,500,222,300,625]
y = [254,512,500,541,625]
unique = []
for i in x:
    if i in y:
         unique.append(i)
         pass
print(unique ,"are unique")"""


"""x = [120,500,300,50,40,40]


for i in x:
    if x.count(i)>1: 
       
        #x1.append(i)
       print("not unique")
    else:
     print("unique")  
 
#unique = x and x 
#for i in x:
     
        
      #unique.append(i)  
#print(unique)"""
"""x1 = [ ]

def arg(*args):
    for i in args:

        if i in args:
             
             x1.append(i)
print(arg(1,1,2,5,4,7,4,4))  
print(x1)"""      


x  = [4,5,6]

y = set(x)
#print(y)
#for i in x:
if len(x)== len(y):
    print(" unique")
else:
    print("not unique") 