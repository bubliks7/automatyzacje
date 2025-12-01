import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/999999")

if response.status_code == 200:
    try:
        dane = response.json()
        print("OK - pobrano dane")
    except ValueError as e:
        print("Błąd parsowania JSON: ", e)

else:
    print("Błąd API, kod:", response.status_code)

