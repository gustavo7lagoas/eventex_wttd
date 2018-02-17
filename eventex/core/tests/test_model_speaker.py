from django.test import TestCase
from eventex.core.models import Speaker
from django.shortcuts import resolve_url as r


class ModelSpeakerTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            description='Almirante e Programadora',
            website='http://hbn.link/hopper-site',
            photo='http://hbn.link/hopper-pic',
            slug='grace-hopper'
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_description_can_be_blank(self):
        description = Speaker._meta.get_field('description')
        self.assertTrue(description.blank)

    def test_website_can_be_blank(self):
        website = Speaker._meta.get_field('website')
        self.assertTrue(website.blank)

    def test_str(self):
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_get_absolute_url(self):
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())