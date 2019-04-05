import json
from random import randint
from unittest import mock

from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse

from payparts.use_cases import GetRedirectUrlUseCase
from payparts.models import Log
from payparts.settings import API_REDIRECT_URL
from payparts.views import PayPartsCallbackView


class GetRedirectUrlUseCaseTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            "order_id": f"order-{randint(1, 1000000)}",
            "amount": 400.00,
            "parts_count": 6,
            "merchant_type": "PP",
            "products": [
                {
                    "name": "Телевизор",
                    "count": 2,
                    "price": 100.00
                },
                {
                    "name": "Микроволновка",
                    "count": 1,
                    "price": 200.00
                }
            ],
            "response_url": "http://shop.com/response",
            "redirect_url": "http://shop.com/redirect",
        }

    def test_success_payment_create(self):
        redirect_url = GetRedirectUrlUseCase().execute(self.data)
        self.assertEqual(Log.objects.count(), 1)
        log = Log.objects.first()
        self.assertEqual(log.type, 'payment_create')
        self.assertEqual(
            log.token,
            redirect_url.split('?')[-1].split('=')[-1]
        )
        self.assertEqual(
            redirect_url,
            f'{API_REDIRECT_URL}?token={log.token}'
        )


class PayPartsCallbackViewTestCase(TestCase):
    def setUp(self) -> None:
        self.url = reverse('pay-parts:callback')
        self.factory = RequestFactory()
        self.data = {
            "status": "canceled",
            "message": "Клиент не завершил оплату",
            "orderId": "254",
            "storeId": "191C85A7FE8743B7BA19",
            "signature": "r9B3fKjTz/qDLfh11Vs9t+izCVI=",
            "paymentState": "CANCELED"
        }

    def test_view(self):
        request = self.factory.post(
            self.url,
            data=json.dumps(self.data),
            content_type='application/json'
        )
        with mock.patch('payparts.signals.pay_parts_success_callback.send', autospec=True) as mocked_handler:
            response = PayPartsCallbackView.as_view()(request)
            self.assertEqual(json.loads(response.content), self.data)
            self.assertEqual(Log.objects.count(), 1)
            log = Log.objects.first()
            self.assertEqual(log.type, 'callback')
            self.assertEquals(mocked_handler.call_count, 1)
            mocked_handler.assert_called_with(sender=Log, log=Log.objects.first(), request=request)
