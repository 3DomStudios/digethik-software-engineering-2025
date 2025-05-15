import requests

# Name deines Wohnorts – z.B. Berlin, Hamburg, München
ort = "Berlin"

# API-Endpunkt für die Geocoding-Abfrage
url = "https://geocoding-api.open-meteo.com/v1/search"

# Anfrage mit dem Ortsnamen
params = {
    "name": ort,
    "count": 1,         # Nur den besten Treffer
    "language": "de",   # Antwort auf Deutsch (optional)
    "format": "json"
}

# HTTP GET-Anfrage
response = requests.get(url, params=params)
print(response.status_code)
data = response.json()
# print(data)


latitude = data['results'][0]['latitude']
longitude = data['results'][0]['longitude']
print(f'latitude: {latitude}')
print(f'longitude: {longitude}')


# Koordinaten von deinem Wohnort (Beispiel: Berlin)
latitude = 52.52
longitude = 13.41

# API-Endpunkt für Wettervorhersage
url = "https://api.open-meteo.com/v1/forecast"

# Parameter: tägliche Vorhersage für Temperatur & Wettercode
params = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "temperature_2m_max,temperature_2m_min,weathercode",
    "timezone": "Europe/Berlin"
}

# Anfrage senden
response = requests.get(url, params=params)

# Antwort prüfen und ausgeben
if response.status_code == 200:
    data = response.json()
    print("Wettervorhersage für die nächsten 5 Tage:\n")
    for i in range(5):
        datum = data["daily"]["time"][i]
        t_min = data["daily"]["temperature_2m_min"][i]
        t_max = data["daily"]["temperature_2m_max"][i]
        code = data["daily"]["weathercode"][i]
        print(f"{datum}: {t_min}°C – {t_max}°C, Wettercode: {code}")
else:
    print("Fehler beim Abrufen der Wetterdaten:", response.status_code)


# Koordinaten deines Wohnorts – Beispiel: Berlin
latitude = 52.52
longitude = 13.41

# Datum für die historische Abfrage
start_date = "2019-03-08"
end_date = "2019-03-08"

# API-Endpunkt
url = "https://archive-api.open-meteo.com/v1/archive"

# Anfrageparameter: tägliche Temperatur und Wettercode
params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": start_date,
    "end_date": end_date,
    "daily": "temperature_2m_min,temperature_2m_max,weathercode",
    "timezone": "Europe/Berlin"
}

# Anfrage ausführen
response = requests.get(url, params=params)

# Antwort verarbeiten
if response.status_code == 200:
    data = response.json()
    datum = data["daily"]["time"][0]
    t_min = data["daily"]["temperature_2m_min"][0]
    t_max = data["daily"]["temperature_2m_max"][0]
    code = data["daily"]["weathercode"][0]

    print(f"Wetter am {datum} in Berlin:")
    print(f"  Temperatur: {t_min}°C – {t_max}°C")
    print(f"  Wettercode: {code}")
else:
    print("Fehler beim Abrufen der historischen Wetterdaten:", response.status_code)
