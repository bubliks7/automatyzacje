import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/2")

dane = response.json()

if dane["completed"] == True:
    print("Zadanie zakończone - nic nie robię")
else:
    print("Zadanie NIE jest zakończone - zgłaszam do systemu")
