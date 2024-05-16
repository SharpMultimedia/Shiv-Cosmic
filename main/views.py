import requests
import base64
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings    
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        day = int(request.POST.get('day'))
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        hour = int(request.POST.get('hour'))
        minute = int(request.POST.get('min'))
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        tzone = request.POST.get('tzone')
        language = request.POST.get('language')
        place = request.POST.get('place')

        # Validate and convert lat, lon, tzone to float
        try:
            lat = float(lat)
            lon = float(lon)
            tzone = float(tzone)
        except ValueError as e:
            print(f"Error converting to float: {e}")
            messages.error(request, "Invalid location data.")
            return render(request, 'index.html')

        # Save form data to session
        request.session['form_data'] = {
            'name': name,
            'gender': gender,
            'day': day,
            'month': month,
            'year': year,
            'hour': hour,
            'minute': minute,
            'lat': lat,
            'lon': lon,
            'language': language,
            'tzone': tzone,
            'place': place
        }

        return redirect('payment')

    days = list(range(1, 32))
    months = list(range(1, 13))
    years = list(range(1900, 2025))
    years.reverse()
    hours = list(range(0, 24))
    minutes = list(range(0, 60))

    return render(request, 'index.html', {
        'days': days,
        'months': months,
        'years': years,
        'hours': hours,
        'minutes': minutes
    })

def payment(request):
    form_data = request.session.get('form_data', {})
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        
        # Save mobile and email to session
        request.session['mobile'] = mobile
        request.session['email'] = email

        return redirect('process_payment')

    return render(request, 'payment.html', {'form_data': form_data})

def process_payment(request):
    # Here you would integrate with a payment gateway.
    # For simplicity, we'll assume the payment is always successful.

    form_data = request.session.get('form_data')
    mobile = request.session.get('mobile')
    email = request.session.get('email')

    if not form_data:
        return redirect('index')

    # Your API credentials
    userId = '4545'
    apiKey = 'ByVOIaODH57QRVi6CqswHXGlcpDvj7tZBRoorY'

    # API endpoint
    api = 'basic_horoscope_pdf'
    url = "https://pdf.astrologyapi.com/v1/" + api

    # Data to be sent in the request
    data = {
        'name': form_data['name'],
        'gender': form_data['gender'],
        'day': form_data['day'],
        'month': form_data['month'],
        'year': form_data['year'],
        'hour': form_data['hour'],
        'min': form_data['minute'],
        'lat': form_data['lat'],
        'lon': form_data['lon'],
        'language': form_data['language'],
        'tzone': form_data['tzone'],
        'place': form_data['place'],
        'chart_style': 'EAST_INDIAN',
        'footer_link': 'shivcosmic.com',
        'logo_url': 'https://static.wixstatic.com/media/84af2a_7e90f12303024e74a4e8a10f9edb1802~mv2.png/v1/crop/x_0,y_2,w_512,h_508/fill/w_161,h_160,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/App%20icon_2_512X512_edited.png',
        'company_name': 'Shiv Cosmic',
        'company_info': '(Unit of Natural Healing and Meditation Center) \n an ISO 9000:2015 Certified Organization',
        'domain_url': 'https://www.shivcosmic.com',
        'company_email': 'info.nhmcpune@gmail.com',
        'company_landline': '+91 9175932752',
        'company_mobile': '+91 9175932752',
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
            pdf_url = astrology_data.get('pdf_url')
            print(astrology_data)
            print(data)
            try:
                e_message = (f"Hello,\n Please check the attached link to open the PDF: {pdf_url} \n\n"
                             f"Name: {form_data['name']}\n"
                             f"Birthdate: {form_data['day']}/{form_data['month']}/{form_data['year']}\n"
                             f"Time: {form_data['hour']}:{form_data['minute']}\n"
                             f"Mobile: {mobile}\n"
                             f"Email: {email}\n\n"
                             "Kind Regards\nTeam Sharp Multimedia")
                send_mail(
                    "You Have Received PDF of your request",
                    e_message,
                    settings.EMAIL_HOST_USER,
                    ["sns.it@yahoo.com"],
                    fail_silently=False
                )
                messages.success(request, "Message Was Sent Successfully")
            except BadHeaderError as e:
                # Log or print the exception for debugging
                print(f"Error sending email: {e}")
            return render(request, 'result.html', {'astrology_data': astrology_data})
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("Error:", e)

    return render(request, 'result.html')