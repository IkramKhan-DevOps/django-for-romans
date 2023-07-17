from payments import PaymentStatus

from src.apps.app_payments.models import Payment


def create_waiting_payment(total, capture, delivery=0, tax=0, currency="usd", **kwargs):
    payment = Payment.objects.create(
        variant='stripe',
        status=PaymentStatus.WAITING,
        total=total,
        delivery=delivery,
        tax=tax,
        captured_amount=capture,
        description="Processing checkout, payments are unpaid now",
        currency=currency,
    )
    return payment
