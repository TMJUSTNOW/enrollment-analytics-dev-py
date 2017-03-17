# courses.views

from django.shortcuts import render
from django.conf.urls import url
from django.views.generic import TemplateView, DetailView, ListView

from .models import Course, ClassSchedule


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'


class ClassScheduleListView(ListView):
    model = ClassSchedule
    template_name = 'course_schedule_list.html'

    def get(self, request, *args, **kwargs):       
        return super(ClassScheduleListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        
        
        try: 
            print self.object_list
            self.object_list = self.object_list.filter(semester_title__contains=self.kwargs['year'])
            print self.object_list
        except Exception as e:
            print str(e)
            pass
        context = super(ClassScheduleListView, self).get_context_data(**kwargs)
        return context


