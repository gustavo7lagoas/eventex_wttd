from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """ GET / must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use index.html """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """ Must show keynote speakers """
        contents = [
            "Grace Hopper",
            "http://hbn.link/hopper-pic",
            "Alan Turing",
            "http://hbn.link/turing-pic"
        ]
        for expect in contents:
            with self.subTest():
                self.assertContains(self.response, expect)

    def test_speakers_link(self):
        """ Must contain link to speakers section """
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def test_nav_items(self):
        """ Must check navegation menu """
        navegation_menu = [
            'href="{}#overview"'.format(r('home')),
            'href="{}#speakers"'.format(r('home')),
            'href="{}#sponsors"'.format(r('home')),
            'href="{}#register"'.format(r('home')),
            'href="{}#venue"'.format(r('home'))
        ]
        for menu_item in navegation_menu:
            with self.subTest():
                self.assertContains(self.response, menu_item)