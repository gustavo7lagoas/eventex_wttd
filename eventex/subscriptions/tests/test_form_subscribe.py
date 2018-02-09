from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """ Form must have 4 fields """
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertListEqual(expected, list(form.fields))
        #self.assertSequenceEqual(expected, list(form.fields))

    def test_name_must_be_capitalized(self):
        """ Name must be capitalized """
        form = self.make_validated_form(name='GUSTAVO fonseca')
        self.assertEqual('Gustavo Fonseca', form.cleaned_data['name'])

    def test_cpf_is_only_digit(self):
        """ CPF must contain only digits """
        form = self.make_validated_form(cpf='ASDF5678901')
        self.assertFormErrorMessage(form, 'cpf', 'CPF must contain only digits')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors.get('email'))

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """ At least phone or email should be informed """
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    # def test_must_inform_email_or_phone_must_use_safe_get(self):
    #     with self.assertRaises(ValidationError):
    #         self.make_validated_form(email='asdf', phone='')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors_list = form.errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Gustavo Fonseca', cpf='12345678901',
                     phone='938654321', email='test@mail.com')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
