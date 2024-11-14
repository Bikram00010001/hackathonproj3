from django.shortcuts import render
from .models import states,fertilizer,Biopesticide,Herbicide,crop
import requests
from datetime import datetime, timedelta
# Create your views here.

def about(request):
    return render(request,'about_us.html',{})

def connect(request):
    return render(request,'connectwithus.html',{})
def index(request):
    states_list = states.objects.all()
    return render(request, 'index.html', {'states': states_list})

def state_crops(request, state_name):
    state = states.objects.get(name=state_name)
    crops = state.crop_id.all()
    return render(request, 'state_crops.html', {'state': state, 'crops': crops})

def expected(request):
    crops=crop.objects.all()
    return render(request,'expectedincome.html',{"crops":crops})
def weather(request):
    if 'city' in request.GET:
        city = request.GET['city']
    else:
        city = "Gurdaspur"  
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": city}
    headers = {
        "X-RapidAPI-Key": "2283810e28msha72b771b039c12ap10f47bjsn12049337ee4e",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    city = data['location']['name']
    current_temperature = data['current']['temp_c']
    current_description = data['current']['condition']['text']
    current_humidity = data['current']['humidity']

    # Get the forecast for the next 4 days
    forecast = []
    for i in range(0, min(len(data['forecast']['forecastday']), 5)):  # Forecast for the next 4 days
        forecast_day = data['forecast']['forecastday'][i]
        forecast.append({
            'date': forecast_day['date'],
            'max_temp': forecast_day['day']['maxtemp_c'],
            'min_temp': forecast_day['day']['mintemp_c'],
            'description': forecast_day['day']['condition']['text']
        })

    context = {
        'city': city,
        'current_temperature': current_temperature,
        'current_description': current_description,
        'current_humidity': current_humidity,
        'forecast': forecast
    }
    return render(request, 'weather.html', context)