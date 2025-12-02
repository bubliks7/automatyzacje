alerty = [
    {"id": 101, "severity": "low"},
    {"id": 102, "severity": "high"},
    {"id": 103, "severity": "medium"},
    {"id": 104, "severity": "high"},
]

for alert in alerty:
    if alert["severity"] == "high":
        print(f"Alert {alert['id']} jest krytyczny - inicjuje akcje")
    elif alert["severity"] == "medium":
        print(f"Alert {alert['id']} wymaga analizy")
    elif alert["severity"] == "low":
        print(f"Alert {alert['id']} o niskim priorytecie - ignoruje")
    else:
        print("error")
