from django.urls import path
from .import views

urlpatterns = [
    path('',views.RegisterAPI.as_view()),
    path('verify',views.VerifyOTP.as_view()),
]
