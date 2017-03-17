"""enrollment_analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from courses.views import CourseListView, ClassScheduleListView
from core.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^courses/$', CourseListView.as_view(), name='course_list'),
    url(r'^schedules/$', ClassScheduleListView.as_view(), name='schedule_list'),
    url(r'^schedules/(?P<year>\d+)/$', ClassScheduleListView.as_view(), name='schedule_list'),
    url(r'^admin/', admin.site.urls),
]