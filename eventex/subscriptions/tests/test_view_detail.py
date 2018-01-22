import uuid

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Gustavo Fonseca',
            cpf='12345678901',
            email='gustavo@mail.com',
            phone='938654321'
        )
        self.response = self.client.get('/inscricao/{}/'.format(self.obj.uid))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.email,
            self.obj.phone
        )
        for content in contents:
            with self.subTest():
                self.assertContains(self.response, content)

class SubscriptionDetailNotFound(TestCase):
    def setUp(self):
        uid = uuid.uuid4()
        self.response = self.client.get('/inscricao/{}/'.format(uid))

    def test_not_found(self):
        self.assertEqual(404, self.response.status_code)