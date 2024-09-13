from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kundali', views.index, name='index'),
    path('payment/', views.payment, name='payment'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_return/', views.payment_return, name='payment_return'),
    path('privacy_policy/', views.policy, name='policy'),
    path('terms_condition/', views.terms, name='terms'),
    path('return_and_refund/', views.returnrefund, name='return'),
    path('reikhi_healing/', views.reikhihealing, name='reikhihealing'),
]
