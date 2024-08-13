import requests
import os

def fetch_weather(city):
    # Clé API pour accéder aux données d'OpenWeatherMap
    api_key = "b79a2ad8b34cb155f9d27362e0ee9422"
    
    # URL de base pour l'API OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Paramètres de la requête, incluant la ville, la clé API, et l'unité de température
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    # Effectue la requête GET à l'API OpenWeatherMap
    response = requests.get(base_url, params=params)
    
    # Vérifie si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Convertit la réponse en JSON
        data = response.json()
        # Affiche les données météo
        display_weather(data)
    else:
        # Affiche un message d'erreur si la requête a échoué
        print(f"Error: Unable to fetch data for {city}. Status code: {response.status_code}")

def display_weather(data):
    # Récupère le nom de la ville
    city = data['name']
    
    # Récupère la température actuelle
    temperature = data['main']['temp']
    
    # Récupère la description de la météo
    weather_description = data['weather'][0]['description']
    
    # Affiche les informations météo
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {weather_description.capitalize()}")

if __name__ == "__main__":
    # Demande à l'utilisateur d'entrer le nom de la ville
    city = input("Enter city name: ")
    # Appelle la fonction pour récupérer et afficher les données météo
    fetch_weather(city)
