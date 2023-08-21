#4.	Create a simple calculator that can perform addition, subtraction, multiplication, and division.	
while True:
 def calc(a,b):


  if "add" in x1 :
   add1  =a+b
   print("The addition of two number is:", add1)
   
    
  
  elif "sub" in x1:
   sub1  =a-b
   print("The subtraction of two number is:",sub1)
      
  elif "mul" in x1:
   mul1  =a*b
     
   print("The multiplication of two number is:",mul1)
    
  elif "div" in x1:
    div1  =a/b
   
    print  ("The  division of two number is:",div1 )
     
  else:
    print("Enter the currect number")    

 x1  = "add"
 x1 = "sub"
 x1  = "mul"
 x1 = "div"


 
 print("---------Welcome to Calculator-----------")
 x1 = (input("List of operators:\n -->add\n--> sub\n--> mul\n--> div\n--> select any one of theme, to enter here:"))
 print (x1)
 a = int(input("Enter the first number"))
 b = int(input("Enter the second number"))
 calc(a,b)