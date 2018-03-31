from django.test import TestCase

from eventex.core.admin import SpeakerModelAdmin, admin, ContactInline, TalkModelAdmin
from eventex.core.models import Speaker, Contact, Talk, Course


class SpeakerModelAdminTest(TestCase):
    def setUp(self):
        self.model_admin = SpeakerModelAdmin(Speaker, admin)
        self.speaker = Speaker.objects.create(
            name='Gustavo Fonseca',
            slug='gustavo-fonseca',
            photo='http://hbn.link/armandinho-pic',
            website='http://hbn.link/hopper-site'
        )
        self.speaker.contact_set.create(kind=Contact.EMAIL,
                                        value='gustavo@mail.com')
        self.speaker.contact_set.create(kind=Contact.PHONE,
                                        value='938654321')

    def test_website_link(self):
        site_link = "http://hbn.link/hopper-site"
        expected = '<a href="{0}">{0}</a>'.format(site_link)
        self.assertEqual(expected, self.model_admin.website_link(self.speaker))

    def test_speaker_img(self):
        expected = '<img src="http://hbn.link/armandinho-pic" width="32px" />'
        self.assertEqual(expected, self.model_admin.speaker_img(self.speaker))

    def test_has_inlines(self):
        self.assertIn(ContactInline, self.model_admin.inlines)

    def test_email(self):
        expected = 'gustavo@mail.com'
        self.assertEqual(expected, str(self.model_admin.email(self.speaker)))

    def test_phone(self):
        expected = '938654321'
        self.assertEqual(expected, str(self.model_admin.phone(self.speaker)))


class TalkModelAdminTest(TestCase):
    def test_get_queryset(self):
        model_admin = TalkModelAdmin(Talk, admin)
        talk = Talk.objects.create(
            title='Título'
        )
        course = Course.objects.create(
            title='Outro título',
            slots=15
        )
        speaker = Speaker.objects.create(
            name='Gustavo Fonseca',
            slug='gustavo-fonseca',
            photo='http://hbn.link/armandinho-pic',
            website='http://hbn.link/hopper-site'
        )
        talk.speakers.add(speaker)
        course.speakers.add(speaker)
        self.assertQuerysetEqual(model_admin.get_queryset(None), [repr(talk)])
