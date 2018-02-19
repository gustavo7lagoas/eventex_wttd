from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ModelContactsTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Gustavo Fonseca',
            photo='http://hbn.link/henrique-pic',
            slug='gustavo-fonseca'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker, kind=Contact.EMAIL, value='gustavo@mail.com'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker, kind=Contact.PHONE, value='351938654321'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """ Contact should be limited to phone or email """
        contact = Contact.objects.create(
            speaker=self.speaker, kind='A', value='test'
        )
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker, kind=Contact.EMAIL, value='gustavo@mail.com'
        )
        self.assertEqual('Gustavo Fonseca', str(contact))
