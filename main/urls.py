from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kundali-form/', views.horoscopeform, name='horoscopeform'),
    path('pro-kundali-form/', views.prohoroscopeform, name='prohoroscopeform'),
    path('numerology-form/', views.numerologyform, name='numerologyform'),
    path('astromapping-form/', views.astromappingform, name='astromappingform'),
    path('kundali/', views.kundali, name='kundali'),
    path('payment/', views.payment, name='payment'),
    path('basic_horoscope/', views.basic_horoscope, name='basic_horoscope'),
    path('pro_horoscope/', views.pro_horoscope, name='pro_horoscope'),
    path('payment_return/', views.payment_return, name='payment_return'),
    path('redirect_url/', views.redirect_url, name='redirect_url'),
    path('privacy_policy/', views.policy, name='policy'),
    path('terms_condition/', views.terms, name='terms'),
    path('return_and_refund/', views.returnrefund, name='return'),
    path('workshop/', views.reikhihealing, name='reikhihealing'),
    path('contact_us/', views.contact, name='contact'),
    path('getkundali/', views.getkundali, name='getkundali'),
    path('numerology/', views.numerology, name='numerology'),
    path('pro_numerology/', views.pro_numerology, name='pro_numerology'),
    path('astro_mapping/', views.astro_mapping, name='astro_mapping'),
    path('astro_vastu/', views.astro_vastu, name='astro_vastu'),
    path('bookappointment/', views.bookappointment, name='bookappointment'),
    path('booksession/', views.bookastro, name='bookastro'),
    path('book_astro_payment_return/', views.book_astro_payment_return, name='book_astro_payment_return'),
]