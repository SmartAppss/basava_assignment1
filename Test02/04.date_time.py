#4.	Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.
from datetime import datetime

x = datetime.today()
print(x)

x2 = x.strftime("%d/%m/%Y")
print(x2)

x3 = datetime.now()
x4 = x3.strftime("%H-%M-%S")
print(x4)
