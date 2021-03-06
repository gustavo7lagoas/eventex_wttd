from django.test import TestCase
from pip._vendor.distlib.database import _Cache

from eventex.core.managers import PeriodManager
from eventex.core.models import Talk, Course


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title='Título da Palestra')

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speaker(self):
        """ Talk has many speakers and vice-versa """
        self.talk.speakers.create(name='Gustavo Fonseca',
                                 slug='gustavo-fonseca',
                                 photo='http://hbn.link/turing-pic')
        self.assertEqual(1, self.talk.speakers.count())

    def test_description_can_be_blank(self):
        description = Talk._meta.get_field('description')
        self.assertTrue(description.blank)

    def test_start_can_be_blank(self):
        start = Talk._meta.get_field('start')
        self.assertTrue(start.blank)

    def test_start_null(self):
        start = Talk._meta.get_field('start')
        self.assertTrue(start.null)

    def test_speakers_can_be_blank(self):
        speakers = Talk._meta.get_field('speakers')
        self.assertTrue(speakers.blank)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))

    def test_ordering(self):
        self.assertListEqual(['start'], Talk._meta.ordering)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning talk', start='11:59')
        Talk.objects.create(title='Afternoon talk', start='12:00')

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['Morning talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        qs = Talk.objects.at_afternoon()
        expected = ['Afternoon talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Título do Curso',
            start='09:00',
            slots=20
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_has_speaker(self):
        """
        Test relation between course and speakers
        Course has many speakers and vice-versa
        """
        self.course.speakers.create(
            name='Gustavo Fonseca',
            slug='gustavo-fonseca',
            photo='http://hbn.link/turing-pic'
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual('Título do Curso', str(self.course))

    def test_manager(self):
        self.assertIsInstance(Course.objects, PeriodManager)

    def test_ordering(self):
        self.assertListEqual(['start'], Talk._meta.ordering)
