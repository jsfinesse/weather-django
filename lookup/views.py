from unicodedata import category
from django.shortcuts import render


def home(request):
    import json
    import requests

    api_request = requests.get(
        "http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid={env(API_KEY)}")
    try:
        res = json.loads(api_request.content)
    except Exception as e:
        res = "Error..."

    if res['list'][0]['main']['aqi'] == 1:
        category_desc = "Good"
        category_color = "good"
    elif res['list'][0]['main']['aqi'] == 2:
        category_desc = "Fair"
        category_color = "fair"
    elif res['list'][0]['main']['aqi'] == 3:
        category_desc = "Moderate"
        category_color = "moderate"
    elif res['list'][0]['main']['aqi'] == 4:
        category_desc = "Poor"
        category_color = "poor"
    elif res['list'][0]['main']['aqi'] == 5:
        category_desc = "Very Poor"
        category_color = "verypoor"
    
    return render(request, 'home.html', {'res': res, 'category_desc': category_desc, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
