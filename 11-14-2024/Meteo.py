import requests
import geocoder

# Funzione per ottenere la latitudine e la longitudine tramite l'indirizzo IP
def get_location():
    g = geocoder.ip('me')
    return g.latlng if g.latlng else (None, None)

# Funzione per ottenere le previsioni meteo
def get_weather_forecast(latitude, longitude, days, include_wind, include_precipitation):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
    }
    
    # Aggiungi opzioni in base alla scelta dell'utente
    if include_wind:
        params["daily"] += ",windspeed_10m_max"
    if include_precipitation:
        params["daily"] += ",precipitation_sum"
        
    # Ottieni dati per il numero di giorni scelto
    params["forecast_days"] = days

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Errore nella richiesta meteo:", response.status_code)
        return None

# Funzione principale
def main():
    latitude, longitude = get_location()
    
    if not latitude or not longitude:
        print("Impossibile ottenere la posizione. Verifica la connessione Internet.")
        return
    
    # Input dell'utente per le opzioni di visualizzazione
    print("Scegliere il numero di giorni per le previsioni (1, 3, o 7): ")
    days = int(input("Giorni: "))
    
    include_wind = input("Vuoi visualizzare la velocità del vento? (s/n): ").strip().lower() == 's'
    include_precipitation = input("Vuoi visualizzare le precipitazioni? (s/n): ").strip().lower() == 's'
    
    # Ottenere e mostrare le previsioni
    forecast_data = get_weather_forecast(latitude, longitude, days, include_wind, include_precipitation)
    
    if forecast_data:
        print(f"\nPrevisioni per i prossimi {days} giorni:")
        for day, temp_max, temp_min, wind, precipitation in zip(
                forecast_data["daily"]["time"],
                forecast_data["daily"]["temperature_2m_max"],
                forecast_data["daily"]["temperature_2m_min"],
                forecast_data["daily"].get("windspeed_10m_max", []),
                forecast_data["daily"].get("precipitation_sum", [])
        ):
            print(f"Data: {day}")
            print(f"Temperatura Max: {temp_max}°C, Temperatura Min: {temp_min}°C")
            if include_wind:
                print(f"Velocità del vento: {wind} km/h")
            if include_precipitation:
                print(f"Precipitazioni: {precipitation} mm")
            print("-" * 20)
    else:
        print("Errore nel recupero delle previsioni meteo.")

if __name__ == "__main__":
    main()
