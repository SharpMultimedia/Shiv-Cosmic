from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kundali', views.index, name='index'),
    path('payment/', views.payment, name='payment'),
    path('basic_horoscope/', views.basic_horoscope, name='basic_horoscope'),
    path('pro_horoscope/', views.pro_horoscope, name='pro_horoscope'),
    path('payment_return/', views.payment_return, name='payment_return'),
    path('privacy_policy/', views.policy, name='policy'),
    path('terms_condition/', views.terms, name='terms'),
    path('return_and_refund/', views.returnrefund, name='return'),
    path('reikhi_healing/', views.reikhihealing, name='reikhihealing'),
    path('contact_us/', views.contact, name='contact'),
    path('getkundali', views.getkundali, name='getkundali'),
]
