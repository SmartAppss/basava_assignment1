#6.	Create a program that simulates a basic ATM machine, allowing users to deposit, withdraw, and check their balance. 
depo_amunt = 8000

def depo(depo_amunt):
    
    x  =int(input("Enter the Deposit amount:"))
    
    depo_amunt += x
    

    print( depo_amunt )
    return depo_amount

def witd(depo_amunt):
    
    y = int(input("Enter the withdrow amount:"))
    
    depo_amunt = depo_amunt - y
     
    print("balence is :",depo_amunt)
    return depo_amount

def bal(depo_amunt):
    b =  depo_amunt
    print (b)
    return depo_amount
    


while True:
    print("01.deposit\n","02.withdrow\n","03.balence\n","04.exit")

    x1 = int(input("select any one:"))

    if x1==1:
        data1  =witd(depo_amunt)
        depo_amunt = data1
        depo(depo_amunt)

    elif x1==2:
        data1  =witd(depo_amunt)
        depo_amunt = data1
    elif x1 == 3:
        bal(depo_amunt)        
    elif x1 == 4:
        break
            
        
        
 

