from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/')
def getWeather():
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2b8bd8ea752bde2fb17774a395b3ffbe"
    location = request.values.get("country")

    if location == None:
        location = "sao paulo"

    r = requests.get(url.format(location))
    location_weather = json.loads(r.text)

    weather = {

        'local_name': location_weather['name'],
        'temp': location_weather['main']['temp'],
        'feels_like': location_weather['main']['feels_like'],
        'description': location_weather['weather'][0]['description'],
        'icon': "http://openweathermap.org/img/wn/" + location_weather['weather'][0]['icon'] + ".png"

    }
    return render_template("weather.html", weather=weather)