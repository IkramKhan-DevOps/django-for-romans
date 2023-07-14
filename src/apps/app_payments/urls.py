from django.contrib import admin
from django.urls import path
from .views import payment_details, PaymentCreateView

app_name = "payments"
urlpatterns = [
    path('<int:pk>/detail/', payment_details, name='payment_details'),
    path('create/', PaymentCreateView.as_view(), name='payment_create'),
]
