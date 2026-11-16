from pydantic import BaseModel, Field
from datetime import datetime


class Coord(BaseModel):
    lat: float
    lon: float


class City(BaseModel):
    id: int
    name: str
    coord: Coord
    country: str
    population: int | None = None
    timezone: int  # scarto da UTC in secondi
    sunrise: datetime  # arriva come timestamp unix, Pydantic lo converte
    sunset: datetime


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Clouds(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float | None = None


class Rain(BaseModel):
    # nel JSON la chiave si chiama "3h", che non è un nome Python valido
    mm_3h: float = Field(alias="3h")


class Sys(BaseModel):
    pod: str  # "d" giorno, "n" notte


class ForecastItem(BaseModel):
    dt: datetime
    main: Main
    weather: list[Weather]
    clouds: Clouds
    wind: Wind
    visibility: int | None = None
    pop: float  # probabilità di precipitazioni, da 0 a 1
    rain: Rain | None = None
    sys: Sys
    dt_txt: str


class Forecast(BaseModel):
    cod: str
    message: float
    cnt: int
    items: list[ForecastItem] = Field(
        alias="list"
    )  # "list" è anche una funzione built-in
    city: City
