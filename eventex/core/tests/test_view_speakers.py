from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        self.obj = Speaker.objects.create(
            name='Grace Hopper',
            website='http://hbn.link/hopper-site',
            photo='http://hbn.link/hopper-pic',
            description='Programadora e almirante',
            slug='grace-hopper'
        )
        self.response = self.client.get(r('speaker_detail', slug='grace-hopper'))
    def test_get(self):
        """ GET should return status 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Should render speaker detail template """
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def test_html(self):
        contents = [
            self.obj.name,
            self.obj.description,
            self.obj.photo,
            self.obj.website
        ]
        for expect in contents:
            with self.subTest():
                self.assertContains(self.response, expect)

    def test_context(self):
        """ Should have a speaker context """
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)
