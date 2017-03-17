from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from courses.models import Course, ClassSchedule


class HomeView(TemplateView):
    template_name = 'home.html'