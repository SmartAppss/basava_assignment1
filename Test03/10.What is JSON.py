#JSON is a syntax for storing and exchanging data.

#JSON is text, written with JavaScript object notation.
import json
#canvert json to python
x  ='{"name":"raj","age":20}'

y  =json.loads(x)
print(y["age"])

#conevrting python to json
x  ={"name":"raj","age":20}

y = json.dumps(x)
print(y)


mylist = [-4,6,8,-7]
y  =(all(abs(ele)>2 for ele in mylist ))
print(y)


x1 = compile('print(20)','test','eval')
exec(x1)

class person:
    name = "raj"
    age = 20
#x = getattr(person,"age")
#delattr(person,"age")
#print(x)
#x =getattr(person,"name")
setattr(person,"age",45)
x = getattr(person, "age")
print(x)

def s(seq):
    list = ["e","i","o","u","v"]
    if seq in list:
        return True
    else:
        return False
seq = ["s","a","r","t","g","e"]
filterd = filter(s,seq) 
for i in filterd:
    print(i)   

x = "print(22,44,55)"
exec(x) 
words_str = input("Enter a list of words, separated by spaces: ")
value = list(input("enter the value: "))
words = {word: value for word in( words_str.split(),value*2)}
print(words)



