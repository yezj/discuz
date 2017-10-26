# -*- coding: utf-8 -*-

import datetime
import hashlib
from django.db import models
from django.utils.text import ugettext_lazy as _
from positions import PositionField
from django.db.models.signals import post_save, post_delete
from django.core.exceptions import ValidationError
# from filebrowser.fields import FileBrowseField, FileObject
from django.contrib.auth.models import User as AdminUser


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=20)
    slug = models.SlugField(_('Slug'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')
        ordering = ('slug',)

    def __unicode__(self):
        return self.title


class Advert(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True)
    title = models.CharField(_('Title'), max_length=50)
    timestamp = models.DateTimeField(auto_now=True, verbose_name=_('timestamp'))
    description = models.TextField(_('Description'), blank=True)
    # ad = FileBrowseField(
    #     _('Ad'), max_length=200, directory='img/ad',
    #     format='image', extensions=[".jpg"], blank=True)
    url = models.URLField(blank=True, verbose_name=_('url'))
    created_at = models.DateTimeField(auto_now_add=True)
    edit_at = models.DateTimeField(verbose_name=_('Edit_at'), default=datetime.datetime.now)

    class Meta:
        verbose_name = _('Advert')
        verbose_name_plural = _('Advert')
        ordering = ('-timestamp',)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=128)
    adverts = models.ManyToManyField(Advert, through='AdvertShip')

    def __unicode__(self):  # __unicode__ on Python 2
        return self.name


class AdvertShip(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    position = PositionField(_('Position'), collection='section')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AdvertShip'
        verbose_name_plural = _('AdvertShips')
        ordering = ('position',)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.advert.title
