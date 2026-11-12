import requests

api_key = "a294b419d929993414e4627a289b1b48"

# https://openweathermap.org/api/forecast5?collection=current_forecast#other

def get_forecast(citta):
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast", 
            {"q":citta, "appid":api_key})
    except:
        print("Errore")