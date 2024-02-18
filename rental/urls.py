from django.urls import path
from rental.views.auth import (
    EmailVerficationView,
    LoginView
)
from rental.views.apartment import AddApartmentView

urlpatterns = [
    path('auth/verify/', EmailVerficationView.as_view(), name='email_verification'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('apartment/add/', AddApartmentView.as_view(), name='add_apartment')
    ]