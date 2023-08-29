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

