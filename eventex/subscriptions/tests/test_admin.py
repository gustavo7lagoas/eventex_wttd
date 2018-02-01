from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.admin import SubscriptionModelAdmin, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        self.model_admin = SubscriptionModelAdmin(Subscription, admin)
        Subscription.objects.create(
            name='Gustavo',
            cpf='12345678901',
            email='test@mail.com',
            phone='938654321'
        )

    def test_has_action(self):
        """ Action mark_as_paid should be installed """
        self.assertIn('mark_as_paid', self.model_admin.actions)


    def test_mark_all(self):
        """ It should mark all selected subscription as paid """
        self.call_action_mark_as_paid()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())


    def test_message(self):
        """ It should send message to the user """
        mock = self.call_action_mark_as_paid()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como pago')


    def call_action_mark_as_paid(self):
        selected_subscriptions = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, selected_subscriptions)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock