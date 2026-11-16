import requests
from pydantic import ValidationError
from models.forecast import Forecast

api_key = "a294b419d929993414e4627a289b1b48"

# https://openweathermap.org/api/forecast5?collection=current_forecast#other


# type hint
def get_forecast(citta: str) -> tuple[int, Forecast | None]:
    status_code = 0

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast",
            {"q": citta, "appid": api_key, "units": "metric", "lang": "it"},
        )

        response.raise_for_status()

        status_code = response.status_code

        if status_code != 200:
            return status_code, None

        return response.status_code, Forecast.model_validate(response.json())
    except ValidationError as e:
        print(f"Risposta non conforme:\n{e}")
        return status_code, None
    except requests.exceptions.RequestException as e:
        print(e)
        return status_code, None
