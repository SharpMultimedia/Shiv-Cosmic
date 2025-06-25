import requests
import time
import base64
import json
import hashlib
import shortuuid
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings    
from django.contrib import messages
from .models import *

import urllib
from urllib.request import urlopen,Request
import json


def home(request):
    return render(request, 'NewLandingpage.html')

def kundali(request):
    return render(request, 'Newkundli.html')

def bookappointment(request):
    return render(request, 'bookappointment.html')

def horoscopeform(request):
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
        place = request.POST.get('place', 'Default')

        # Validate and convert lat, lon, tzone to float
        try:
            lat = float(lat)
            lon = float(lon)
            tzone = float(tzone)
        except ValueError as e:
            print(f"Error converting to float: {e}")
            messages.error(request, "Invalid location data.")
            return render(request, 'kundali.html')

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

    return render(request, 'buykundali.html', {
        'days': days,
        'months': months,
        'years': years,
        'hours': hours,
        'minutes': minutes
    })

def prohoroscopeform(request):
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
        place = request.POST.get('place', 'Default')

        # Validate and convert lat, lon, tzone to float
        try:
            lat = float(lat)
            lon = float(lon)
            tzone = float(tzone)
        except ValueError as e:
            print(f"Error converting to float: {e}")
            messages.error(request, "Invalid location data.")
            return render(request, 'kundali.html')

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

    return render(request, 'prokundaliform.html', {
        'days': days,
        'months': months,
        'years': years,
        'hours': hours,
        'minutes': minutes
    })

def numerologyform(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        day = int(request.POST.get('day'))
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        language = request.POST.get('language')

        # Save form data to session
        request.session['form_data'] = {
            'name': name,
            'gender': gender,
            'day': day,
            'month': month,
            'year': year,
            'language': language,
        }

        return redirect('payment')

    days = list(range(1, 32))
    months = list(range(1, 13))
    years = list(range(1900, 2025))
    years.reverse()
    hours = list(range(0, 24))
    minutes = list(range(0, 60))

    return render(request, 'numerologyform.html', {
        'days': days,
        'months': months,
        'years': years,
        'hours': hours,
        'minutes': minutes
    })

def astromappingform(request):
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
        place = request.POST.get('place', 'Default')

        # Validate and convert lat, lon, tzone to float
        try:
            lat = float(lat)
            lon = float(lon)
            tzone = float(tzone)
        except ValueError as e:
            print(f"Error converting to float: {e}")
            messages.error(request, "Invalid location data.")
            return render(request, 'kundali.html')

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

    return render(request, 'astromappingform.html', {
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

        kundliType = request.POST.get('kundliType', None)
        print(kundliType)

        if kundliType == "Basic Kundli":
            amount = 299
        elif kundliType == "Pro Kundli":
            amount = 499
            
        elif kundliType == "Pro Numerology":
            amount = 699
        elif kundliType == "Astro-Vastu":
            amount = 999
        # Construct the dynamic URLs
        base_url = request.build_absolute_uri('/')
        redirectUrl = base_url + 'payment_return/'
        callbackUrl = base_url + 'payment_return/'

        url = "https://api.phonepe.com/apis/hermes/pg/v1/pay"
        MERCHANT_ID = "M22REVYZNMPVY"
        MERCHANT_USER_ID = "MUID123"
        REDIRECT_URL = redirectUrl
        CALLBACK_URL = callbackUrl
        API_KEY = "71dedcf7-11d5-461a-bb1c-a5bc7231b45f"
        ENDPOINT = "/pg/v1/pay"
        INDEX = '2' 
        payload = {
            "merchantId": MERCHANT_ID,
            "merchantTransactionId": shortuuid.uuid(),
            "merchantUserId": MERCHANT_USER_ID,
            "amount": amount * 100,  # Amount in paise
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

        try:
            response = requests.post(url, headers=headers, json=json_data, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            response_data = response.json()
            print(response_data)
            request.session['mobile'] = mobile
            request.session['email'] = email
            request.session['kundliType'] = kundliType
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            messages.error(request, "There was an error processing your payment. Please try again.")
            return render(request, 'payment.html', {'form_data': form_data})

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
    INDEX = "2"
    SALTKEY = "71dedcf7-11d5-461a-bb1c-a5bc7231b45f"
    merchantId = "M22REVYZNMPVY"
    # url = "https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/pay"
    # SALTKEY = "14fa5465-f8a7-443f-8477-f986b8fcfde9"
    # merchantId = "PGTESTPAYUAT77"
    form_data = request.POST
    form_data_dict = dict(form_data)
    transaction_id = form_data.get('transactionId', None)
    print(transaction_id)
    print("Form dict : ")
    print(form_data)

    # Retrieve kundli_type from the session
    kundliType = request.session.get('kundliType', None)
    print(f"Kundli Type: {kundliType}")

    # Check the payment status
    payment_status = form_data.get('code', None)

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
        try:
            response = requests.get(request_url, headers=headers, timeout=10)
            response_data = response.json()
            print(response_data)
             
            if payment_status == 'PAYMENT_SUCCESS':
                return redirect('redirect_url')
            else:
                messages.error(request, "Payment was unsuccessful. Please try again.")
                return redirect('home')  # Redirect to index if payment is unsuccessful

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            messages.error(request, "There was an error retrieving the payment status. Please try again.")
            return redirect('home')  # Redirect to index if there's a request exception
    else:
        messages.error(request, "Invalid transaction ID.")
    return render(request, 'Kundali.html', {'form_data': form_data})

def redirect_url(request):
    kundliType = request.session.get('kundliType', None)
    print(kundliType)
    if kundliType == "Basic Kundli":
        return redirect('basic_horoscope')
    elif kundliType == "Pro Kundli":
        return redirect('pro_horoscope')
    elif kundliType == "Pro Numerology":
        return redirect('pro_numerology')
    elif kundliType == "Astro-Vastu":
        return redirect('astro_vastu')
    else:
        messages.error(request, "Invalid Kundli type. Please try again.")
        return redirect('home')  # Redirect to index if kundli_type is invalid

def basic_horoscope(request):
    # Here you would integrate with a payment gateway.
    # For simplicity, we'll assume the payment is always successful.

    form_data = request.session.get('form_data')
    mobile = request.session.get('mobile')
    email = request.session.get('email')
    report_name = "Basic Kundali"

    if not form_data:
        return redirect('index')

    # Check if the API response is already in the session
    astrology_data = request.session.get('astrology_data')
    pdf_content_b64 = request.session.get('pdf_content_b64')

    if not astrology_data or not pdf_content_b64:
        # Your API credentials
        userId = '616659'
        apiKey = '73d704711428670b973f180f43b26f92'
        print("in kundali loop")
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
            'minute': form_data['minute'],
            'latitude': form_data['lat'],
            'longitude': form_data['lon'],
            'language': form_data['language'],
            'timezone': form_data['tzone'],
            'place': form_data['place'],
            'chart_style': 'NORTH_INDIAN',
            'footer_link': 'shivcosmic.com',
            'logo_url': 'https://static.wixstatic.com/media/84af2a_7e90f12303024e74a4e8a10f9edb1802~mv2.png/v1/crop/x_0,y_2,w_512,h_508/fill/w_161,h_160,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/App%20icon_2_512X512_edited.png',
            'company_name': 'Shiv Cosmic',
            'company_info': '(Unit of Natural Healing and Meditation Center) \n an ISO 9000:2015 Certified Organization',
            'domain_url': 'https://www.shivcosmic.com',
            'company_email': 'info.nhmcpune@gmail.com',
            'company_landline': '+91 7030127129',
            'company_mobile': '+91 7030127129',
        }

        # Authorization header
        auth = "Basic " + base64.b64encode((userId + ":" + apiKey).encode()).decode()

        headers = {
            "Authorization": auth,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200:
                # Process the response data here
                astrology_data = response.json()
                pdf_url = astrology_data.get('pdf_url')

                # Download the PDF file
                pdf_response = requests.get(pdf_url, timeout=10)
                pdf_response.raise_for_status()
                pdf_content = pdf_response.content
                pdf_content_b64 = base64.b64encode(pdf_content).decode('utf-8')

                Report.objects.create(
                    name=form_data['name'],
                    email=email,
                    mobile=mobile,
                    pdf_url=pdf_url,
                    report_type='Basic Horoscope'
                )

                # Save the astrology data and PDF content to the session
                request.session['astrology_data'] = astrology_data
                request.session['pdf_content_b64'] = pdf_content_b64

                try:
                    email_message = EmailMessage(
                        f"Kundali Report for {form_data['name']}",
                        "Please find the attached PDF document.\n\n"
                        f"Name: {form_data['name']}\n"
                        f"Birthdate: {form_data['day']}/{form_data['month']}/{form_data['year']}\n"
                        f"Time: {form_data['hour']}:{form_data['minute']}\n"
                        f"Mobile: {mobile}\n"
                        f"Email: {email}\n\n"
                        "Kind Regards\nTeam Shiv Cosmic",
                        settings.EMAIL_HOST_USER,
                        [email],
                        cc=["info.shivcosmic@gmail.com"]
                    )

                    # Attach the PDF file
                    email_message.attach('astrology_report.pdf', pdf_content, 'application/pdf')
                    email_message.send()
                    del request.session['astrology_data']
                    del request.session['pdf_content_b64']

                    messages.success(request, "Message Was Sent Successfully")
                except BadHeaderError as e:
                    # Log or print the exception for debugging
                    print(f"Error sending email: {e}")

            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return render(request, 'result.html')
    else:
        messages.info(request, "Your PDF has already been sent to your email. Please check your inbox.")

    return render(request, 'result.html', {'astrology_data': astrology_data,'report_name':report_name})

def pro_horoscope(request):
    # Here you would integrate with a payment gateway.
    # For simplicity, we'll assume the payment is always successful.

    form_data = request.session.get('form_data')
    mobile = request.session.get('mobile')
    email = request.session.get('email')

    report_name = "Pro Kundali"
    
    if not form_data:
        return redirect('index')

    # Check if the API response is already in the session
    astrology_data = request.session.get('astrology_data')
    pdf_content_b64 = request.session.get('pdf_content_b64')

    if not astrology_data or not pdf_content_b64:
        # Your API credentials
        userId = '616659'
        apiKey = '73d704711428670b973f180f43b26f92'
        print("in Pro kundali loop")

        # API endpoint
        api = 'pro_horoscope_pdf'
        url = "https://pdf.astrologyapi.com/v1/" + api

        # First create the authorization header
        auth = "Basic " + base64.b64encode((userId + ":" + apiKey).encode()).decode()

        # Define headers before trying to print them
        headers = {
            "Authorization": auth,
            "Content-Type": "application/json"
        }

        # Data to be sent in the request
        data = {
            'name': form_data['name'],
            'gender': form_data['gender'],
            'day': form_data['day'],
            'month': form_data['month'],
            'year': form_data['year'],
            'hour': form_data['hour'],
            'minute': form_data['minute'],
            'latitude': form_data['lat'],
            'longitude': form_data['lon'],
            'language': form_data['language'],
            'timezone': form_data['tzone'],
            'place': form_data['place'],
            'chart_style': 'NORTH_INDIAN',
            'footer_link': 'shivcosmic.com',
            'logo_url': 'https://sharpmultimedia.in/static/assets/icons/Sharp%20Multimedi%20Pvt.%20Ltd%20Logo%2001.png',
            'company_name': 'Shiv Cosmic',
            'company_info': '(Unit of Natural Healing and Meditation Center) \n an ISO 9000:2015 Certified Organization',
            'domain_url': 'https://www.shivcosmic.com',
            'company_email': 'info.nhmcpune@gmail.com',
            'company_landline': '+91 7030127129',
            'company_mobile': '+91 7030127129',
        }

        # Now print the request data
        print("\n=== API Request Data ===")
        print(f"URL: {url}")
        print("\nHeaders:")
        print(headers)
        print("\nRequest Data:")
        print(json.dumps(data, indent=2))
        print("=====================\n")

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200:
                # Process the response data here
                astrology_data = response.json()
                pdf_url = astrology_data.get('pdf_url')

                # Download the PDF file
                pdf_response = requests.get(pdf_url, timeout=10)
                pdf_response.raise_for_status()
                pdf_content = pdf_response.content
                pdf_content_b64 = base64.b64encode(pdf_content).decode('utf-8')

                Report.objects.create(
                    name=form_data['name'],
                    email=email,
                    mobile=mobile,
                    pdf_url=pdf_url,
                    report_type='Pro Horoscope'
                )

                # Save the astrology data and PDF content to the session
                request.session['astrology_data'] = astrology_data
                request.session['pdf_content_b64'] = pdf_content_b64

                try:
                    email_message = EmailMessage(
                        f"Pro Kundali Report for {form_data['name']}",
                        "Please find the attached PDF document.\n\n"
                        f"Name: {form_data['name']}\n"
                        f"Birthdate: {form_data['day']}/{form_data['month']}/{form_data['year']}\n"
                        f"Time: {form_data['hour']}:{form_data['minute']}\n"
                        f"Mobile: {mobile}\n"
                        f"Email: {email}\n\n"
                        "Kind Regards\nTeam Shiv Cosmic",
                        settings.EMAIL_HOST_USER,
                        [email],
                        cc=["info.shivcosmic@gmail.com"]
                    )

                    # Attach the PDF file
                    email_message.attach('astrology_report.pdf', pdf_content, 'application/pdf')
                    email_message.send()
                    del request.session['astrology_data']
                    del request.session['pdf_content_b64']

                    messages.success(request, "Message Was Sent Successfully")
                except BadHeaderError as e:
                    # Log or print the exception for debugging
                    print(f"Error sending email: {e}")

            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return render(request, 'result.html')
    else:
        messages.info(request, "Your PDF has already been sent to your email. Please check your inbox.")

    return render(request, 'result.html', {'astrology_data': astrology_data, 'report_name':report_name})

def pro_numerology(request):
    form_data = request.session.get('form_data')
    mobile = request.session.get('mobile')
    email = request.session.get('email')
    report_name = "Numerology"

    if not form_data:
        return redirect('index')

    # Check if the API response is already in the session
    astrology_data = request.session.get('astrology_data')
    pdf_content_b64 = request.session.get('pdf_content_b64')
    # del request.session['astrology_data']
    # del request.session['pdf_content_b64']

    if not astrology_data or not pdf_content_b64:
        # Your API credentials
        userId = '616659'
        apiKey = '73d704711428670b973f180f43b26f92'

        # API endpoint
        api = 'pro_numerology_report'
        url = "https://pdf.astrologyapi.com/v1/" + api

        # Data to be sent in the request
        data = {
            'name': form_data['name'],
            'gender': form_data['gender'],
            'day': form_data['day'],
            'month': form_data['month'],
            'year': form_data['year'],
            # 'hour': form_data['hour'],
            # 'minute': form_data['minute'],
            # 'latitude': form_data['lat'],
            # 'longitude': form_data['lon'],
            'language': form_data['language'],
            # 'timezone': form_data['tzone'],
            # 'place': form_data['place'],
            'footer_link': 'shivcosmic.com',
            'logo_url': 'https://shivcosmic.com/static/assets/images/Logo/shiv%20cosmic%20logo%20w.png',
            'company_name': 'Shiv Cosmic',
            'company_info': '(Unit of Natural Healing and Meditation Center) \n an ISO 9000:2015 Certified Organization',
            'domain_url': 'https://www.shivcosmic.com',
            'company_email': 'info.nhmcpune@gmail.com',
            'company_landline': '+91 7030127129',
            'company_mobile': '+91 7030127129',
            'model_name':'THEME_COSMIC'
        }

        # Authorization header
        auth = "Basic " + base64.b64encode((userId + ":" + apiKey).encode()).decode()

        headers = {
            "Authorization": auth,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200:
                # Process the response data here
                astrology_data = response.json()
                if 'response' in astrology_data and 'pdf_url' in astrology_data['response']:
                    # For pro_numerology endpoint
                    pdf_url = astrology_data['response']['pdf_url']
                    # Create a compatible structure
                    astrology_data = {
                        'pdf_url': pdf_url,
                        'response': astrology_data['response']  # Keep original response if needed
                    }

                # Download the PDF file
                pdf_response = requests.get(pdf_url, timeout=10)
                pdf_response.raise_for_status()
                pdf_content = pdf_response.content
                pdf_content_b64 = base64.b64encode(pdf_content).decode('utf-8')

                Report.objects.create(
                    name=form_data['name'],
                    email=email,
                    mobile=mobile,
                    pdf_url=pdf_url,
                    report_type='Pro Numerology'
                )

                # Save the astrology data and PDF content to the session
                request.session['astrology_data'] = astrology_data
                request.session['pdf_content_b64'] = pdf_content_b64

                try:
                    email_message = EmailMessage(
                        f"Pro Numerology Report for {form_data['name']}",
                        "Please find the attached PDF document.\n\n"
                        f"Name: {form_data['name']}\n"
                        f"Birthdate: {form_data['day']}/{form_data['month']}/{form_data['year']}\n"
                        f"Mobile: {mobile}\n"
                        f"Email: {email}\n\n"
                        "Kind Regards\nTeam Shiv Cosmic",
                        settings.EMAIL_HOST_USER,
                        [email],
                        cc=["info.shivcosmic@gmail.com"]
                    )

                    # Attach the PDF file
                    email_message.attach('numerology_report.pdf', pdf_content, 'application/pdf')
                    email_message.send()
                    del request.session['astrology_data']
                    del request.session['pdf_content_b64']

                    messages.success(request, "Message Was Sent Successfully")
                except BadHeaderError as e:
                    # Log or print the exception for debugging
                    print(f"Error sending email: {e}")

            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return render(request, 'result.html')
    else:
        messages.info(request, "Your PDF has already been sent to your email. Please check your inbox.")

    return render(request, 'result.html', {'astrology_data': astrology_data,'report_name':report_name})

def reikhihealing(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        
        # Verify reCAPTCHA v3
        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        
        try:
            # Make request to verify the token
            response = requests.post(url, data=data)
            result = response.json()
            
            # Check if verification was successful and score is above threshold
            if result.get('success') and result.get('score', 0) > 0.5:  # Adjust threshold as needed
                # Create new Rekhi_Form instance
                form = Rekhi_Form(
                    firstname=request.POST.get('firstname'),
                    lastname=request.POST.get('lastname'),
                    phone=request.POST.get('phone'),
                    email=request.POST.get('email'),
                    message=request.POST.get('message')
                )
                form.save()
                messages.success(request, 'Form submitted successfully!')
            else:
                messages.error(request, 'reCAPTCHA verification failed. Please try again.')
        except Exception as e:
            print(f"reCAPTCHA verification error: {e}")
            messages.error(request, 'An error occurred. Please try again.')
        
        return redirect('reikhihealing')

    # Add reCAPTCHA site key to template context
    context = {
        'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY
    }
    return render(request, 'Newreiki.html', context)

def policy(request):
    return render(request, 'policy.html')

def returnrefund(request):
    return render(request, 'return.html')

def terms(request):
    return render(request, 'terms.html')

def getkundali(request):
    return render(request, 'getkundali.html')

def verify_recaptcha(response_token):
    """ Verifies reCAPTCHA token with Google """
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': response_token
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result.get('success', False)

def contact(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        print(recaptcha_response)
        if verify_recaptcha(recaptcha_response):
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            Contact.name = name
            Contact.email = email
            Contact.message = message
            Contact.save()
            messages.success(request, 'Form submitted successfully!')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        
        return redirect('contact')
    
    return render(request, 'Newcontact.html', {
        'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_PUBLIC_KEY
    })

def numerology(request):
    return render(request, 'numerology.html')

def astro_mapping(request):
    return render(request, 'astromapping.html')

def astro_vastu(request):
    form_data = request.session.get('form_data')
    mobile = request.session.get('mobile')
    email = request.session.get('email')
    report_name = "Astromapping"

    if not form_data:
        return redirect('index')

    # Check if the API response is already in the session
    astrology_data = request.session.get('astrology_data')
    pdf_content_b64 = request.session.get('pdf_content_b64')

    if not astrology_data or not pdf_content_b64:
        # Your API credentials
        userId = '616659'
        apiKey = '73d704711428670b973f180f43b26f92'

        # API endpoint
        api = 'custom_abundance_report'
        url = "https://pdf.astrologyapi.com/v1/" + api

        # Data to be sent in the request
        data = {
            'name': form_data['name'],
            'gender': form_data['gender'],
            'day': form_data['day'],
            'month': form_data['month'],
            'year': form_data['year'],
            'hour': form_data['hour'],
            'minute': form_data['minute'],
            'latitude': form_data['lat'],
            'longitude': form_data['lon'],
            'language': form_data['language'],
            'timezone': form_data['tzone'],
            'place': form_data['place'],
            'chart_style': 'NORTH_INDIAN',
            'footer_link': 'shivcosmic.com',
            'logo_url': 'https://shivcosmic.com/static/assets/images/Logo/shiv%20cosmic%20logo%20w.png',
            'company_name': 'Shiv Cosmic',
            'company_info': '(Unit of Natural Healing and Meditation Center) \n an ISO 9000:2015 Certified Organization',
            'domain_url': 'https://www.shivcosmic.com',
            'company_email': 'info.nhmcpune@gmail.com',
            'company_landline': '+91 7030127129',
            'company_mobile': '+91 7030127129',
        }

        # Authorization header
        auth = "Basic " + base64.b64encode((userId + ":" + apiKey).encode()).decode()

        headers = {
            "Authorization": auth,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200:
                # Process the response data here
                astrology_data = response.json()
                pdf_url = astrology_data.get('pdf_url')

                # Download the PDF file
                pdf_response = requests.get(pdf_url, timeout=10)
                pdf_response.raise_for_status()
                pdf_content = pdf_response.content
                pdf_content_b64 = base64.b64encode(pdf_content).decode('utf-8')

                Report.objects.create(
                    name=form_data['name'],
                    email=email,
                    mobile=mobile,
                    pdf_url=pdf_url,
                    report_type='Astro Vastu'
                )

                # Save the astrology data and PDF content to the session
                request.session['astrology_data'] = astrology_data
                request.session['pdf_content_b64'] = pdf_content_b64

                try:
                    email_message = EmailMessage(
                        f"Astro Vastu Report for {form_data['name']}",
                        "Please find the attached PDF document.\n\n"
                        f"Name: {form_data['name']}\n"
                        f"Birthdate: {form_data['day']}/{form_data['month']}/{form_data['year']}\n"
                        f"Time: {form_data['hour']}:{form_data['minute']}\n"
                        f"Mobile: {mobile}\n"
                        f"Email: {email}\n\n"
                        "Kind Regards\nTeam Shiv Cosmic",
                        settings.EMAIL_HOST_USER,
                        [email],
                        cc=["info.shivcosmic@gmail.com"]
                    )

                    # Attach the PDF file
                    email_message.attach('Vastu Report.pdf', pdf_content, 'application/pdf')
                    email_message.send()
                    del request.session['astrology_data']
                    del request.session['pdf_content_b64']

                    messages.success(request, "Message Was Sent Successfully")
                except BadHeaderError as e:
                    # Log or print the exception for debugging
                    print(f"Error sending email: {e}")

            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return render(request, 'result.html')
    else:
        messages.info(request, "Your PDF has already been sent to your email. Please check your inbox.")

    return render(request, 'result.html', {'astrology_data': astrology_data,'report_name':report_name})

def base(request):
    context = {
        'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY
    }
    return render(request, 'base.html', context)

def bookastro(request):
    if request.method == "POST":  
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile') 

        
        new_booking = AstroBooking.objects.create(  
                        name=name, 
                        phone=mobile,  
                        email=email,  
                        paid=False  
                    ) 
        print("id") 
        print(new_booking.id)
        merchant_transaction_id = f"ASTROBOOK_{new_booking.id}_{int(time.time())}"
        print(merchant_transaction_id)
        # Construct the dynamic URLs
        base_url = request.build_absolute_uri('/')
        redirectUrl = f"{base_url}book_astro_payment_return/?merchantTransactionId={merchant_transaction_id}"
        callbackUrl = f"{base_url}book_astro_payment_return/?merchantTransactionId={merchant_transaction_id}"

     
        url = "https://api.phonepe.com/apis/hermes/pg/v1/pay"
        MERCHANT_ID = "M22REVYZNMPVY"
   
        MERCHANT_USER_ID = "MUID123"
        amount = 100  # ₹99.00
        REDIRECT_URL = redirectUrl
        CALLBACK_URL = callbackUrl
        API_KEY = "71dedcf7-11d5-461a-bb1c-a5bc7231b45f"
        ENDPOINT = "/pg/v1/pay"
        INDEX = '2' 
        payload = {
            "merchantId": MERCHANT_ID,
            "merchantTransactionId":merchant_transaction_id,
            "merchantUserId": MERCHANT_USER_ID,
            "amount": amount,
            "redirectUrl": REDIRECT_URL,
            "redirectMode": "POST",
            "callbackUrl": CALLBACK_URL,
            "mobileNumber": "7841888451",
            "paymentInstrument": {
                "type": "PAY_PAGE",
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
        

        if 'data' in response_data and 'instrumentResponse' in response_data['data'] and 'redirectInfo' in response_data['data']['instrumentResponse']:
            return redirect(response_data['data']['instrumentResponse']['redirectInfo']['url'])
        return render(request, 'bookastro.html')
    return render(request, 'bookastro.html')


@csrf_exempt
def book_astro_payment_return(request):
    
    print('payment-return')
    INDEX = "2"
    SALTKEY = "71dedcf7-11d5-461a-bb1c-a5bc7231b45f"
    merchantId = "M22REVYZNMPVY"
    form_data = request.POST
    payment_status = form_data.get('code', None)
    if request.method == 'POST':
        merchantTransactionId = request.POST.get("merchantTransactionId") or request.GET.get("merchantTransactionId")

        print("Returned merchantTransactionId: ", merchantTransactionId)
             
        
        if merchantTransactionId:
            request_url = f"https://api.phonepe.com/apis/hermes/pg/v1/status/{merchantId}/{merchantTransactionId}"
            sha256_Pay_load_String = f'/pg/v1/status/{merchantId}/{merchantTransactionId}{SALTKEY}'
            sha256_val = calculate_sha256_string(sha256_Pay_load_String)
            checksum = sha256_val + '###' + INDEX

            headers = {
                'Content-Type': 'application/json',
                'X-VERIFY': checksum,
                'X-MERCHANT-ID': merchantTransactionId,
                'accept': 'application/json',
            }

            try:
                response = requests.get(request_url, headers=headers)
                response_data = response.json()
                print(response_data)
                # payment_status = response_data.get('code') 
                if payment_status == 'PAYMENT_SUCCESS':
                    try:
                        booking_id = int(merchantTransactionId.split('_')[1])
                    except (IndexError, ValueError) as e:
                        print(f"Invalid merchantTransactionId format: {merchantTransactionId}")
                        messages.error(request, "Invalid transaction ID.")
                        return redirect("/")
                    booking = AstroBooking.objects.filter(id=booking_id).first()
                    if booking:
                        booking.paid = True
                        booking.save()
                    messages.success(request, "Payment Successful! Thank you for your booking.")    
                    return render(request, 'thankyou.html')
                else:
                    messages.error(request, "Payment was unsuccessful. Please try again.", {"response_data": response_data})
                    return render(request, 'bookastro.html')
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                messages.error(request, "Error checking payment status. Please try again.", {"response_data": response_data})
                return render(request, 'bookastro.html')
        else:
            messages.error(request, "Merchant Transaction ID missing in callback.")
    else:
        messages.error(request, "Invalid request method.")
    
    return redirect('home')

