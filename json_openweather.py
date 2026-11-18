import requests
from pydantic import ValidationError
from models.forecast import Forecast
import os

# https://openweathermap.org/api/forecast5?collection=current_forecast#other


# type hint
def get_forecast(citta: str) -> tuple[int, Forecast | None]:
    status_code = 0
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    try:
        if not api_key:
            raise ValueError("OPENWEATHER_API_KEY non trovata")

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
    except ValueError as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(e)

    return status_code, None
