from django.shortcuts import render
import requests

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '9a2efabab38e2f13781f5a1429068e45'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description'],
                'city': city
            }
            return render(request, 'weather/index.html', {'weather': weather_data})
        else:
            return render(request, 'weather/index.html', {'error': 'City not found.'})
    return render(request, 'weather/index.html')




