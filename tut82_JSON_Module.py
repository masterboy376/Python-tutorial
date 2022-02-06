import json

# string to json
data = '{"name":"sam", "occupation":"all"}'
parsed = json.loads(data)
print(parsed['name'])
print(parsed)
# what is json.load 

# dictionary to json 
data1 = {
    "name":"sam",
    "occupation":"all",
    "isGood":True
}
parsed1 = json.dumps(data1)
print(parsed1)
# what is sort_keys parameter in dumps 
