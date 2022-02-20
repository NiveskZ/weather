from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/')
def getWeather():
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2b8bd8ea752bde2fb17774a395b3ffbe"
    country = request.values.get("country")
    r = requests.get(url.format(country))
    country_weather = json.loads(r.text)

    weather = {

        'local_name': country_weather['name'],
        'temp': country_weather['main']['temp'],
        'feels_like': country_weather['main']['feels_like'],
        'description': country_weather['weather'][0]['description'],
        'icon': "http://openweathermap.org/img/wn/" + country_weather['weather'][0]['icon'] + ".png"

    }
    return render_template("weather.html", weather=weather)