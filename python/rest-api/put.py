import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)

todo = {"userId":1, "title":"call John", "compeleted": True}

response = requests.put(api_url, json=todo)

print(response.json())
