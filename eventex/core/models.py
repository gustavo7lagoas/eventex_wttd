from django.db import models
from django.shortcuts import resolve_url as r

from eventex.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    description = models.TextField('descrição', blank=True)
    website = models.URLField('website', blank=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone')
    )

    speaker = models.ForeignKey('Speaker')
    kind = models.CharField(max_length=1, choices=KINDS, verbose_name='tipo')
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField('Título', max_length=255)
    description = models.TextField('Descrição', blank=True)
    start = models.TimeField('Início', blank=True, null=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='Palestrantes',
                                      blank=True)

    objects = PeriodManager()

    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'
        ordering = ['start']

    def __str__(self):
        return self.title


class Course(Talk):
    slots = models.IntegerField()

    objects = PeriodManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
