import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={c}&units=imperial&appid=0d929c7852690622fae3c5445f2cc54e'
           


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        #here we pass city value to c parameter
        r = requests.get(url.format(c=city)).json()


        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
      
            'description' : r['weather'][0]['description'],
     
            'icon' : r['weather'][0]['icon'],
     
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)


{'coord': {'lon': 91.1105, 'lat': 23.9691}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 91.47, 'feels_like': 104.07, 'temp_min': 91.47, 'temp_max': 91.47, 'pressure': 1003, 'humidity': 70}, 'visibility': 4500, 'wind': {'speed': 0, 'deg': 0}, 'clouds': {'all': 75}, 'dt': 1659258464, 'sys': {'type': 1, 'id': 9107, 'country': 'BD', 'sunrise': 1659223446, 'sunset': 1659271179}, 'timezone': 21600, 'id': 1185263, 'name': 'Brahmanbaria', 'cod': 200}