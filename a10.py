import json

y = '{"data":{"name": "John", "age": 30, "city": "New York", "pets": ["dog", "cat"]},"data":{"name": "John", "age": 30, "city": "New York", "pets": ["snake"], "data":{"name": "John", "age": 30, "city": "New York", "pets": ["parrot"], "data":{"name": "John", "age": 30, "city": "New York", "pets": ["parrot2"], "data":{"name": "John", "age": 30, "city": "New York", "pets": ["parrot3"], "data":{"name": "John", "age": 30, "city": "New York", "pets": ["parrot4"]}}}}}}' 
z = json.loads(y)



# x = dict.fromkeys(y)
for x, obj in z.items():
    print(x)
    
    for i in obj:
        print(i + ':', obj[i])