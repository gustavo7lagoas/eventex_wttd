from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class ModelSubscriptionsTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Gustavo Fonseca',
            cpf='12345678901!',
            email='gustavo@mail.com',
            phone='938654321'
        )
        self.obj.save()


    def test_created(self):
        self.assertTrue(Subscription.objects.exists())


    def test_created_at(self):
        """ Subscriptions should have an auto filled created at attribute """
        self.assertIsInstance(self.obj.created_at, datetime)


    def test_str(self):
        self.assertEqual('Gustavo Fonseca', str(self.obj))