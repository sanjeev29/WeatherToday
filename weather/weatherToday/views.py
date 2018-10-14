from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from pprint import pprint
from .models import City
import geocoder
import requests
import datetime

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
    return converted_time

def ajaxer(request):
	if request.is_ajax:
		latitude = request.GET.get('Latitude')
		longitude = request.GET.get('Longitude')
		result = geocoder.opencage([latitude, longitude], key='fdb8ae4a92ae4eebab0ec5a9a2c85e0b', method='reverse')
		#print(result.city, result.state, result.country)
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f009f5c6a0f7ab4448e65aa4b5f3f0c5'
		city_weather = requests.get(url.format(result.city)).json()
		#pprint(city_weather)
		weather = {
			'city': city_weather['name'],
			'country': city_weather['sys']['country'],
			'temperature': city_weather['main']['temp'],
			'main': city_weather['weather'][0]['main'],
			'description': city_weather['weather'][0]['description'],
			'icon': city_weather['weather'][0]['icon'],
			'humidity': city_weather['main']['humidity'],
			'pressure': city_weather['main']['pressure'],
			'sunrise': time_converter(city_weather['sys']['sunrise']),
			'sunset': time_converter(city_weather['sys']['sunset']),
			'wind_speed': city_weather['wind']['speed'],
			'temp_max': city_weather['main']['temp_max'],
			'temp_min': city_weather['main']['temp_min']
	}
	#pprint(weather)
	#return HttpResponse()
	return JsonResponse(weather)	

def home(request):	
	return render(request, 'weather.html')