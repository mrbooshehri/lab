import requests

api_url =  "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)

print(response.json())

todo = {"title": "call John"}

response = requests.patch(api_url, json=todo)

print(response.json())
print(response.status_code)
