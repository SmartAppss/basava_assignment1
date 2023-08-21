#8.	Write a function to find the common elements between two lists without duplicates.

def comm(a,b):
    a_com = set(a)
    b_com = set(b) 

    if (a_com & b_com):
        print(a_com & b_com )
    else: 
        print("no comman words")

a  = (1,2,3,4,6,5)
b = (7,8,5,3,4,6)
comm(a,b) 