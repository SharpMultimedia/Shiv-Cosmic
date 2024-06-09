import requests
import time
import base64
import json
import hashlib
import shortuuid
import datetime
from django.shortcuts import render, redirect
from .models import Payment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings    
from django.contrib import messages
from requests.exceptions import RequestException

def index(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        day = int(request.POST.get('day'))
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        hour = int(request.POST.get('hour'))
        minute = int(request.POST.get('minute'))
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
        
def calculate_sha256_string(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()

def base64_encode(input_dict):
    json_data = json.dumps(input_dict)
    data_bytes = json_data.encode('utf-8')
    return base64.b64encode(data_bytes).decode('utf-8')


def payment(request):
    form_data = request.session.get('form_data', {})
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        
        # Construct the dynamic URLs
        base_url = request.build_absolute_uri('/')
        redirectUrl = base_url + 'payment_return/'
        callbackUrl = base_url + 'payment_return/'

        url = "https://api.phonepe.com/apis/hermes/pg/v1/pay"
        MERCHANT_ID = "M22REVYZNMPVY"
        MERCHANT_USER_ID = "MUID123"
        REDIRECT_URL = redirectUrl
        CALLBACK_URL = callbackUrl
        API_KEY = "f35e2d5a-2d92-4cea-8404-7ef608af3522"
        ENDPOINT = "/pg/v1/pay"
        INDEX = '1'
        payload = {
            "merchantId": MERCHANT_ID,
            "merchantTransactionId": shortuuid.uuid(),
            "merchantUserId": MERCHANT_USER_ID,
            "amount": 1 * 100,  # Amount in paise
            "redirectUrl": REDIRECT_URL,
            "redirectMode": "POST",
            "callbackUrl": CALLBACK_URL,
            "mobileNumber": mobile,
            "paymentInstrument": {
                "type": "PAY_PAGE",
            }
        }

        # Base64 encode the payload
        base64_string = base64_encode(payload)

        # Calculate checksum
        checksum_input = base64_string + "/pg/v1/pay" + "f35e2d5a-2d92-4cea-8404-7ef608af3522"
        checksum = calculate_sha256_string(checksum_input)

        headers = {
            "Content-Type": "application/json",
            "X-VERIFY": checksum + "###1"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("success"):
                payment_url = response_data['data']['instrumentResponse']['redirectInfo']['url']
                return redirect(payment_url)
            else:
                error_message = response_data.get('message', 'Payment initiation failed.')
                return HttpResponse(f"Error initiating payment: {error_message}")

        except RequestException as e:
            print(f"Error initiating payment: {e}")
            return HttpResponse(f"Error initiating payment: {str(e)}")

    return render(request, 'payment.html', {'form_data': form_data})

@csrf_exempt
def payment_return(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        payment_status = request.POST.get('payment_status')

        if payment_status == "Success":
            # Fetch the AstrologyAPI report after successful payment
            return redirect('process_payment')
        else:
            return HttpResponse("Payment failed. Please try again.")

def process_payment(request):
    form_data = request.session.get('form_data', {})

    url = "https://api.vedicrishiastro.com/v1/general_ascendant_report"

    user_id = "622615"
    api_key = "d8cfb4a2b22b0b7f4d4f127fb69cf354"

    payload = {
        'name': form_data.get('name'),
        'gender': form_data.get('gender'),
        'day': form_data.get('day'),
        'month': form_data.get('month'),
        'year': form_data.get('year'),
        'hour': form_data.get('hour'),
        'minute': form_data.get('minute'),
        'lat': form_data.get('lat'),
        'lon': form_data.get('lon'),
        'tzone': form_data.get('tzone'),
        'language': form_data.get('language')
    }

    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{user_id}:{api_key}'.encode('utf-8')).decode('utf-8')}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        # Save or process the astrology report data as needed
        return render(request, 'report.html', {'report': response_data})

    except RequestException as e:
        print(f"Error fetching astrology report: {e}")
        return HttpResponse(f"Error fetching astrology report: {str(e)}")