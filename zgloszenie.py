użytkownicy = [
    {"name": "Adam", "status": "active"},
    {"name": "Ewa", "status": "locked"},
    {"name": "Ola", "status": "active"}
]

for user in użytkownicy:
    if user["status"] == "active":
        print('Uzytkownik ' + user['name'] + ' jest aktywny')
    else:
        print('Uzytkownik ' + user['name'] + ' jest zablokowany - zgłaszam do systemu')
        
