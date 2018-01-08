from django.core import mail
from django.test import TestCase


class SubscribePostTest(TestCase):
    def setUp(self):
        """ Valid post should redirect to /inscricao/ """
        data = dict(name='Gustavo Fonseca', cpf='12345678901',
                    email='test@mail.com', phone='938654321')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'test@mail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Gustavo Fonseca',
            '12345678901',
            'test@mail.com',
            '938654321'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
