"""
        11.      The program that you create for this exercise will begin by reading the cost of a meal
                ordered at a restaurant from the user. Then your program will compute the tax and tip 
                for 	the meal. Use your local tax rate when computing the amount of tax owing. Compute
                the 	tip as 18 percent of the meal amount (without the tax). The output from your 
                program 	should 	include the tax amount, the tip amount, and the grand total for the
                meal including 	both the tax and the tip. Format the output so that all of the values
                are displayed 	using 	two decimal places."""


print("----------well come to meal restaurant-----------")
print("prices of the meal is 100:,200:,250:")
y = int(input("select amount to buy:"))
tip = (18/100)*y

tax = (5/100)*y
tax_meal = y + tax

grand_total = tax_meal + tip
print("Meal price is:",y,"\n","-->5% GST on food services:",tax,"\n","-->18% of Tip is:",tip,"\n","-->Total amount is:",round(grand_total),"\n")
