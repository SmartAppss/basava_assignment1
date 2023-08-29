#8.	Write a function to find the common elements between two lists without duplicates.

def comm(a,b):
    a_com = set(a)
    b_com = set(b) 

    if (a_com & b_com):
        print(a_com & b_com )
    else: 
        print("no comman words")

a  = (14,7,12,8,6,2)
b = (9,5,4,3,7,1)
 
print(any(ele in a for ele in b))

