#10	Area of a Room
#Write a program that asks the user to enter the width and length of a room. Once the values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating point numbers. Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.

x =  float(input("Enter the width of room in floot: "))
y = float(input("Enter the length of room in floot:"))

z = float(x*y)
print("Area of the room is",z,".sq.ft")