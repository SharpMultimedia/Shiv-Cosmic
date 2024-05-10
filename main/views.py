import requests
import base64
import json
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        day = int(request.POST.get('day'))
        month = int(request.POST.get('month'))
        day = int(request.POST.get('day'))
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        hour = int(request.POST.get('hour'))
        minute = int(request.POST.get('min'))
        lat = float(request.POST.get('lat'))
        lon = float(request.POST.get('lon'))
        language = request.POST.get('language')
        tzone = float(request.POST.get('tzone'))
        place = request.POST.get('place')

        # Your API credentials
        userId = '4545'
        apiKey = 'ByVOIaODH57QRVi6CqswHXGlcpDvj7tZBRoorY'

        # API endpoint
        api = 'basic_horoscope_pdf'
        url = "https://pdf.astrologyapi.com/v1/" + api

        # Data to be sent in the request
        data = {
            'name':name,
            'gender':gender,
            'day': day,
            'month': month,
            'year': year,
            'hour': hour,
            'min': minute,
            'lat': lat,
            'lon': lon,
            'language':language,
            'tzone': tzone,
            'place':place,
            'chart_style':'EAST_INDIAN',
            'footer_link':'shivcosmic.com',
            'logo_url':'https://static.wixstatic.com/media/84af2a_7e90f12303024e74a4e8a10f9edb1802~mv2.png/v1/crop/x_0,y_2,w_512,h_508/fill/w_161,h_160,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/App%20icon_2_512X512_edited.png',
            'company_name':'Shiv Cosmic',
            'company_info':'(Unit of Natural Healing and Meditation Center) \n an ISO 9000:2015 Certified Organization',
            'domain_url':'https://www.shivcosmic.com',
            'company_email':'info.nhmcpune@gmail.com',
            'company_landline':'+91 9175932752',
            'company_mobile':'+91 9175932752',
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

