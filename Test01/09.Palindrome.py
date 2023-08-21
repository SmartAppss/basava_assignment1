#9.	Write a function that checks whether a given string is a palindrome (reads the same forwards and backwards).

x  = "madam"
z = x
y = (x[ :: -1])
if  z == y:
 print(y,"is palindrome")
else:
 print( x, "is not palindrome") 