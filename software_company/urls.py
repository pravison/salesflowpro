
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingPage, name='landing_page'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:id>', views.service, name='service'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('thank-you/', views.thankYou, name='thank_you'),
    path('lead', views.leads, name='lead'),
    path('terms-of-service/', views.termsOfService, name='terms_of_service'),
    path('privacy-policy/', views.privacyPolicy, name='privacy_policy')
]