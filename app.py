import requests
import argparse
import pyfiglet
from simple_chalk import chalk

# API key from openweathmap
Api_Key = "Write your API key"

# Base URL for openweathermap API
Base_Url = "https://api.openweathermap.org/data/2.5/weather"

# Map the weather codes to weather icons
Weather_Icons = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

#Construct API URL with query parameters
parser = argparse.ArgumentParser(description="Check the weather for a certain Country/City")
parser.add_argument("Country", help="The Country/City to check the weather for")
args = parser.parse_args()
url = f"{Base_Url}?q={args.Country}&appid={Api_Key}&units=metric"

#Make API request and parse response using requests module
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()

#Parsing the JSON response from the API and extract the weather information.
data = response.json()

#Get the information from response
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

#Construct the output with weather icons
weather_icon = Weather_Icons.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon}  {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

#Print the output
print(chalk.yellow(output))