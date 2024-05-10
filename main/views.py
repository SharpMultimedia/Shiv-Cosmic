import requests
import base64
import json
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Get form data
        day = int(request.POST.get('day'))
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        hour = int(request.POST.get('hour'))
        minute = int(request.POST.get('min'))
        lat = float(request.POST.get('lat'))
        lon = float(request.POST.get('lon'))
        tzone = float(request.POST.get('tzone'))

        # Your API credentials
        userId = '630368'
        apiKey = '62aa3fc1f8c8134be63409f206d0133c8c2f383a'

        # API endpoint
        api = 'birth_details'
        url = "https://json.astrologyapi.com/v1/" + api

        # Data to be sent in the request
        data = {
            'day': day,
            'month': month,
            'year': year,
            'hour': hour,
            'min': minute,
            'lat': lat,
            'lon': lon,
            'tzone': tzone,
        }

        # Authorization header
        auth = "Basic " + base64.b64encode((userId + ":" + apiKey).encode()).decode()

        headers = {
            "Authorization": auth,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                # Process the response data here
                astrology_data = response.json()
                print(astrology_data)
                return render(request, 'result.html', {'astrology_data': astrology_data})
            else:
                print("Error:", response.status_code)
        except Exception as e:
            print("Error:", e)

    return render(request, 'index.html')

