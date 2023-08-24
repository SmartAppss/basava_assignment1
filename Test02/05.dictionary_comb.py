#5.	Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. Output the new dictionary
from collections import ChainMap
a = {"a":1,"b":3}
b = {"c":3, "b":4}

for i in a:
    if i in b:
        data=(a.update({i:a.get(i)+b.get(i)}))
        b.pop(i)
a.update(b.items())
print(a)
  
        



#data = dict(zip((a1.get("a"),a1.get("b")),(b2.get("c"),b2.get("b"))))
#print(data)


#Bank_New_Schemes.update({'scheme3': ['benifit1_updated', 'benefit2_updated']})


"""x  ={1:2, 2:4}
y = {1:6,2:4}

for i in x:
    if i in y:
        data =( x.update({i:x.get(i)+y.get(i)}))
        y.pop(i)
x.update(y.items())
print(x)"""        