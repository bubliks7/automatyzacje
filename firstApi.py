import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
dane = response.json()

print(dane["title"])
print(dane["completed"])
