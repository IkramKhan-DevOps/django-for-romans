from django.contrib import admin
from django.urls import path

from src.apps.app_payments.views import CheckoutView, PaymentSuccessView, PaymentFailureView, CheckoutProcessView

app_name = "payments"
urlpatterns = [

    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("checkout/<int:pk>/process/", CheckoutProcessView.as_view(), name="checkout_process"),
    path("success/", PaymentSuccessView.as_view(), name="payment_success"),
    path("failure/", PaymentFailureView.as_view(), name="payment_failure"),

]
