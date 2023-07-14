from decimal import Decimal

from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views import View
from payments import get_payment_model, RedirectNeeded
from payments.forms import PaymentForm, CreditCardPaymentForm

from src.apps.app_payments.models import Payment


class PaymentCreateView(View):

    def get(self, request):

        form = CreditCardPaymentForm()

        return TemplateResponse(
            request,
            'app_payments/payment.html',
            {'form': form}
        )

    def post(self, request):
        form = CreditCardPaymentForm(request.POST)
        if form.is_valid():

            payment = Payment.objects.create(
                variant='default',  # this is the variant from PAYMENT_VARIANTS
                description='Book purchase',
                total=Decimal(120),
                tax=Decimal(20),
                currency='USD',
                delivery=Decimal(10),
                billing_first_name='Sherlock',
                billing_last_name='Holmes',
                billing_address_1='221B Baker Street',
                billing_address_2='',
                billing_city='London',
                billing_postcode='NW1 6XE',
                billing_country_code='GB',
                billing_country_area='Greater London',
                customer_ip_address='127.0.0.1',
            )

            # 2: capture the payments from client
            try:
                payment.capture()  # Perform the payment processing

                # Perform additional actions with the payment object if needed
                # For example, update the order status, generate an invoice, etc.
                # Redirect to the confirmation page
                print("everything is done")
                return redirect('confirmation', payment_id=payment.pk)
            except RedirectNeeded as redirect_to:
                return redirect(str(redirect_to))
            except Exception as e:
                print(e)
                return print(e)

        return TemplateResponse(
            request,
            'app_payments/payment.html',
            {'form': form}
        )


def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return TemplateResponse(
        request,
        'app_payments/payment.html',
        {'form': form, 'payment': payment}
    )
