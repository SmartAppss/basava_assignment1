#7.	Write a function that takes a sentence as input and returns the reverse of each word while maintaining the word order.
#x = (input("write a sentence:"))
#for i in x: 
#z = x.index("l")
#print(z)
x = input("enter the sentence:")
#li = [ ]
s = x.split( )
for i in s:
        z = i[ :: -1]
        #li.append(z)
        print(" ".join(z),end = "  ")
#--------------------------------- 
#x2  = (x[ 4:0:-1])

#x3 = (x[10:5:-1])
#x4 = (x[13:10: -1])
#x5 = (x[19:13:-1])
#print(x2,x3,x4,x5)