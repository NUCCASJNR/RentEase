from django.urls import path
from rental.views.auth import EmailVerficationView
from rental.views.auth import LoginView

urlpatterns = [
    path("auth/verify/",
         EmailVerficationView.as_view(),
         name="email_verification"),
    path("auth/login/", LoginView.as_view(), name="login"),
]
