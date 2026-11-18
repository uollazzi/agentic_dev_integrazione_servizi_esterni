import json_placeholder
import json_openweather
import json_tavily
from dotenv import load_dotenv

load_dotenv()

r = json_placeholder.get_users()

print("Status Code:", r[0])

for u in r[1]:
    print(u["name"])

status, forecast = json_openweather.get_forecast("Roma,IT")

if forecast:
    print(forecast.city.name, forecast.city.country)
    for m in forecast.items[:4]:
        print(
            m.dt.strftime("%d/%M/%Y %H"),
            f"{m.main.temp:.1f} °C",
            m.weather[0].description,
        )
else:
    print("Dati non disponibili")


search_result = json_tavily.search("Cosa fa Elon Musk?")
for r in search_result.results:
    print(f"- {r.title}")
