from decimal import Decimal
from typing import Iterable
from payments import PurchasedItem
from payments.models import BasePayment
from core.settings import PAYMENT_HOST, PAYMENT_USES_SSL
from django.db import models


class Payment(BasePayment):

    def get_host_url(self) -> str:
        protocol = 'https://' if PAYMENT_USES_SSL else 'http://'
        return protocol + PAYMENT_HOST

    def get_failure_url(self) -> str:
        return f"{self.get_host_url()}/payments/{self.pk}/failure"

    def get_success_url(self) -> str:
        return f"{self.get_host_url()}/payments/{self.pk}/success"

    def get_purchased_items(self) -> Iterable[PurchasedItem]:
        yield PurchasedItem(
            name='product_name',
            sku='product_sku',
            quantity=9,
            price=Decimal(10),
            currency='USD',
        )
