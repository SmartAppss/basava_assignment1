#10.  Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
#import random
x = {"a":4,"b":5,"c":6,"d":9,"e":10}
#data=sorted(x.values())
#print(data[-3::])
data  =list(x.values())
data.sort()
result = data[-3::]
print(result)

def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s==%s" %(key, value))


# Driver code

myFun(x =1,y=2)


list = [2,"hello",1,"hi", 2,"well come"]


x = " ".join(map(str,list))
print(x) 



