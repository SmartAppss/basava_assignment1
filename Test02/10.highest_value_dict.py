#10.  Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
#import random
x = {"a":4,"b":5,"c":6,"d":9,"e":10}
#data=sorted(x.values())
#print(data[-3::])
data  =list(x.values())
data.sort()
result = data[-3::]
print(result)



