#03:what is generator.
#generator  is like a normal funtion but it use the keyward yeild rather the return  to iterator the values


def fun_generator():
	yield "Hello world!!"
	yield "Geeksforgeeks"


obj = fun_generator()

print(type(obj))

print(next(obj))
print(next(obj))




def inf_sequence():
	num = 0
	while True:
		yield num
		num += 1
		
for i in inf_sequence():
	print(i, end=" ")


	
