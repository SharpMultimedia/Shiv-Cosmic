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

        url = "https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/pay"
        MERCHANT_ID = "PGTESTPAYUAT77"
        MERCHANT_USER_ID = "MUID123"
        REDIRECT_URL = redirectUrl
        CALLBACK_URL = callbackUrl
        API_KEY = "14fa5465-f8a7-443f-8477-f986b8fcfde9"
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
                "type": "PAY_PAGE"
            }
        }

        # Base64 encode the payload
        base64_string = base64_encode(payload)

        # Calculate checksum using API key
        sha256_val = calculate_sha256_string(base64_string + ENDPOINT + API_KEY)
        check_sum = sha256_val + '###' + INDEX

        headers = {
            "accept": "application/json",
            'X-VERIFY': check_sum,
            "Content-Type": "application/json"
        }

        json_data = {
            'request': base64_string,
        }

        response = requests.post(url, headers=headers, json=json_data)
        response_data = response.json()
        print(response_data)
        request.session['mobile'] = mobile
        request.session['email'] = email
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            return HttpResponse(f"Failed to decode JSON response:\n{response.text}", status=response.status_code)

        if 'data' in response_data and 'instrumentResponse' in response_data['data'] and 'redirectInfo' in response_data['data']['instrumentResponse']:
            return redirect(response_data['data']['instrumentResponse']['redirectInfo']['url'])
        else:
            return HttpResponse(f"Payment request failed: {response.text}", status=response.status_code)
    else:
        return render(request, 'payment.html', {'form_data': form_data})

@csrf_exempt     
def payment_return(request):
    print('payment-return')
    INDEX = "1"
    SALTKEY = "bc723c15-6ff9-40b4-a959-d161ef663df2"
    merchantId = "WOODSONLINE"
    form_data = request.POST
    form_data_dict = dict(form_data)
    transaction_id = form_data.get('transactionId', None)
    print(transaction_id)
    if transaction_id:
        request_url = f'https://api.phonepe.com/apis/hermes/pg/v1/status/{merchantId}/{transaction_id}'
        sha256_Pay_load_String = f'/pg/v1/status/{merchantId}/{transaction_id}{SALTKEY}'
        sha256_val = calculate_sha256_string(sha256_Pay_load_String)
        checksum = sha256_val + '###' + INDEX

        headers = {
            'Content-Type': 'application/json',
            'X-VERIFY': checksum,
            'X-MERCHANT-ID': transaction_id,
            'accept': 'application/json',
        }
        response = requests.get(request_url, headers=headers)
        response_data = response.json()
        print(response_data)
         
        return redirect('process_payment')

def process_payment(request):
    # Here you would integrate with a payment gateway.
    # For simplicity, we'll assume the payment is always successful.

    form_data = request.session.get('form_data')
    mobile = request.session.get('mobile')
    email = request.session.get('email')

    print(email,mobile + "This is test")

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

            # Download the PDF file
            pdf_response = requests.get(pdf_url)
            pdf_content = pdf_response.content

            try:
                email_message = EmailMessage(
                    "You Have Received PDF of your request",
                    "Please find the attached PDF document.\n\n"
                    f"Name: {form_data['name']}\n"
                    f"Birthdate: {form_data['day']}/{form_data['month']}/{form_data['year']}\n"
                    f"Time: {form_data['hour']}:{form_data['minute']}\n"
                    f"Mobile: {mobile}\n"
                    f"Email: {email}\n\n"
                    "Kind Regards\nTeam Sharp Multimedia",
                    settings.EMAIL_HOST_USER,
                    ["sns.it@yahoo.com", email],
                )

                # Attach the PDF file
                email_message.attach('astrology_report.pdf', pdf_content, 'application/pdf')
                email_message.send()

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