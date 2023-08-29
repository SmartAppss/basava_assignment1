#1.	Write python function which takes a variable number of arguments.
def arg1(*args):
    mul  = 1
    #mul_up  = [ ]
    for num in args:

        mul = num*mul
        #mul_up.append(mul)
    return mul
result  =arg1(1, 2, 5)
print(result) 

result1 = arg1(10,2,2)
print(result1)





