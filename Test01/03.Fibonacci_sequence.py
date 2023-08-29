#3.	Write a program that prints the Fibonacci sequence up to a given number of terms.
x  = int(input("enter the number:"))

y  = range(x)
num1 = 0
num2 = 1
next_num = 0
for i in y:
    if x == x:
       #num1,num2=num2,numnext_num 
       num1 = num2
       num2 = next_num
       
       next_num = num1 + num2
       print(next_num)  

