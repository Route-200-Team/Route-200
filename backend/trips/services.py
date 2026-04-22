import requests
import os


def get_weather(city):
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial",
        "cnt": 5,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def get_amadeus_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": os.environ.get("AMADEUS_API_KEY"),
        "client_secret": os.environ.get("AMADEUS_API_SECRET"),
    }

    response = requests.post(url, data=data, timeout=10)
    response.raise_for_status()
    return response.json()["access_token"]


def get_flights(origin, destination, date):
    token = get_amadeus_token()

    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": date,
        "adults": 1,
        "max": 10,
        "currencyCode": "USD",
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    return response.json()