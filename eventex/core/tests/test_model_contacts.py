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
        Contact.objects.create(
            speaker=self.speaker, kind=Contact.EMAIL, value='gustavo@mail.com'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            speaker=self.speaker, kind=Contact.PHONE, value='351938654321'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """ Contact should be limited to phone or email """
        contact = Contact(
            speaker=self.speaker, kind='A', value='test'
        )
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker, kind=Contact.EMAIL, value='gustavo@mail.com'
        )
        self.assertEqual('gustavo@mail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(name='Gustavo Fonseca', slug='gustavo-fonseca',
                          photo='http://hbn.link/arnaldinho-pic')
        speaker.contact_set.create(kind=Contact.EMAIL,
                                   value='gustavo@mail.com')
        speaker.contact_set.create(kind=Contact.PHONE,
                                   value='938654321')

    def test_emails(self):
        query_set = Contact.objects.emails()
        expected = ['gustavo@mail.com']
        self.assertQuerysetEqual(query_set, expected, lambda o: o.value)

    def test_phones(self):
        query_set = Contact.objects.phones()
        expect = ['938654321']
        self.assertQuerysetEqual(query_set, expect, lambda o: o.value)
