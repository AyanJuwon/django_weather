import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a492ad1b4c6b66fe32e0e4073b85a00e'
    # city = 'London'


    if request.method == 'POST':
        print(request.POST)
        form = CityForm(request.POST)
        form.save()
        

    form = CityForm()


    cities = City.objects.all()    

    weather_data = []
    
    for city in cities:

        r = requests.get(url.format(city)).json()


        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
                
            }
        weather_data.append(city_weather)

    print(r)
    
    # print(weather_data[3])
    context = {'weather_data' : weather_data, 'form': form}
    # print(context)
    return render(request, 'weather/home.html',context)