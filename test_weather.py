import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

city = "Chennai"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

print("STATUS:", response.status_code)
print(response.json())
