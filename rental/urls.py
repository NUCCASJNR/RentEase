from django.urls import include, path
from rental.views.auth import EmailVerficationView

urlpatterns = [
    path('auth/verify/', EmailVerficationView.as_view(), name='email_verification')
    ]