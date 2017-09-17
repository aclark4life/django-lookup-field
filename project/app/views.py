# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Thing

class ThingDetailView(DetailView):

    model = Thing

    def get_context_data(self, **kwargs):
        context = super(ThingDetailView, self).get_context_data(**kwargs)
        return context


class ThingListView(ListView):

    model = Thing

    def get_context_data(self, **kwargs):
        context = super(ThingListView, self).get_context_data(**kwargs)
        return context
