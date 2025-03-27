from django.conf import settings

def recaptcha(request):
    return {
        'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY
    } 