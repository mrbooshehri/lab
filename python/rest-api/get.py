import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)

# check if response body contains something
if requests.text is not None:
    print("response.json():")
    print(response.json())
    print("response.status_code:")
    print(response.status_code)
    print("response.headers[\"Content-Type\"]")
    print(response.headers["Content-Type"])
