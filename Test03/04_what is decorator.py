#what is decorator
#using decorator to add some extra futures with existing funtion, if the perticular funtion in diffrent file without tuching we can change.

#this funtion in diffrent file 



#here when i am dividng 4/2 ans will be 2 but when i am passing first parameter has 2 and second one has 4 then the  result will be 0.5 to over come this using decorator without tuching original function

#first we have to create a new funtion for decorator

def new_decorator(func): #this func is act like parameter witch is original funtion

    #now create inner funtion to do some logic
    def inner_logic(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner_logic
@ new_decorator # this decorator 
def func1(a,b):
    print(a/b)
func1(2,4) #01 whenever this func1 called it well be called new_decorator and this new_decorator take this funtion as input parameter and respective code will be executed.
#updated_result = new_decorator(func1)  
#updated_result(2,4)



  
             
