import requests

# because of using data keyword you should add this standard library to serialize data
import json

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId":1, "title":"call David", "completed":False}
headers = {"Contetn-Type":"application/json"}

# using json keyword

#response = requests.post(api_url,json=todo)

#using data keyword
## here you need to specify content-type and also you should serialize data
## yous need to pass header as a dictionary format

response= requests.post(api_url, data=json.dumps(todo),headers=headers)

print("response.json():")
print(response.json())
print("response.status_code:")
print(response.status_code)
