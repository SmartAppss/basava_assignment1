"""7.	Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary :"""


dic1={1:10, 2:20}
dic2={3:30, 2:40}
dic3={5:50,2:60}





dic1.update(dic2)
dic1.update(dic3)

print(dic1)

#or------------

"""dict4 = dic1 | dic2 | dic3
print(dict4)

from collections import ChainMap

dic1={1:10, 2:20}
dic2={3:30, 2:40}
dic3={5:50,2:60}

dict4 = ChainMap(dic1,dic2,dic3)

print(dict4)"""