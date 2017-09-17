# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Thing(models.Model):
    """
    """
    def __str__(self):
        return 'thing-%s' % self.pk
