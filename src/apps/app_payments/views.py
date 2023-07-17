from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

import stripe
from payments import PaymentStatus

from .bll import create_waiting_payment
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_delivery_amount():
    return 0


def get_tax_amount():
    return 0


def get_total_amount():
    return 0


def get_capture_amount():
    return 0


def get_amounts():
    return get_total_amount() or 0, get_capture_amount() or 0,  get_delivery_amount() or 0, get_tax_amount() or 0


class CheckoutView(View):

    def get(self, request):
        payment = create_waiting_payment(10, 10, 0, 0, "usd")
        context = {'payment': payment}
        return render(request, "app_payments/checkout.html", context)


class CheckoutProcessView(View):

    def get(self, request, pk):
        """
        complete checkout process for stripe only
        """

        # 1: get values
        host = self.request.get_host()
        total, capture, delivery, tax = get_amounts()
        # 2: get payment [pre auth]
        payment = get_object_or_404(Payment, id=pk)

        # 3: create checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": payment.currency,
                        "unit_amount": int(payment.captured_amount * 100),
                        "product_data": {
                            "name": "Product Name",
                        },
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url='http://' + host + reverse('payments:payment_success') \
                        + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://{}{}'.format(host, reverse(
                'payments:payment_failure')),
        )

        # 4: save session adn payments [pre auth]
        session_id = checkout_session['id']
        payment.transaction_id = session_id
        payment.status = PaymentStatus.PREAUTH
        payment.save()

        # 5: redirect to check out session url
        return redirect(checkout_session.url, code=303)


class PaymentSuccessView(View):
    def get(self, request):
        session_id = request.GET.get("session_id")
        try:
            payment = Payment.objects.get(transaction_id=session_id)
        except Payment.DoesNotExist:
            messages.error(request, "Payment record not found")
            return redirect("payments:payment_failure")

        payment.status = PaymentStatus.CONFIRMED
        payment.save()

        return render(request, "app_payments/success.html")


class PaymentFailureView(View):
    def get(self, request):
        session_id = request.GET.get("session_id")

        try:
            payment = Payment.objects.get(transaction_id=session_id)
        except Payment.DoesNotExist:
            return render(request, "app_payments/failure.html")

        payment.status = PaymentStatus.ERROR
        payment.save()

        return render(request, "app_payments/failure.html")
