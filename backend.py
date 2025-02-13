import os
import requests
import pandas

API_KEY = os.getenv("openweather")

def get_data(place, forecast_days):
    if API_KEY is None:
        raise ValueError("API key must be provided")

    url = (f"http://api.openweathermap.org/data/2.5/forecast"
           f"?q={place}"
           f"&appid={API_KEY}")

    response = requests.get(url)

    if response.status_code != 200:
        return "none"

    data = response.json()

    if "list" not in data:
        raise Exception("Invalid response structure")

    filtered_data = data["list"]
    nr_values = 8 * forecast_days # Because data every 3 hours, 24 hours in a day leads to 8 data points
    filtered_data = filtered_data[:nr_values]

    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=1))