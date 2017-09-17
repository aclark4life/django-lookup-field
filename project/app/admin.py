# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Thing

# Register your models here.

@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    """
    """
