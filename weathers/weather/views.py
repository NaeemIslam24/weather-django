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
