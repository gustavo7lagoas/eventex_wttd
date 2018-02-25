from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Talk, Speaker


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(title='Título da Palestra',
                            description='Descrição da Palestra',
                            start='10:00')
        t2 = Talk.objects.create(title='Título da Palestra',
                            description='Descrição da Palestra',
                            start='13:00')
        speaker = Speaker.objects.create(name='Gustavo Fonseca',
                                         slug='gustavo-fonseca',
                                         photo='http://hbn.link/turing-pic')
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        self.response = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (2, 'Gustavo Fonseca'),
            (2, 'Descrição da Palestra'),
            (2, '<a href="/palestrantes/gustavo-fonseca/"'),
            (1, '10:00'),
            (1, '13:00')
        ]
        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']
        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)

class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))
        contents = (
            'Não há palestras cadastradas para a manhã',
            'Não há palestras cadastradas para a tarde'
        )
        for expected in contents:
            with self.subTest():
                self.assertContains(response, expected)