from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    """Model information about a course."""
    department = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=512)
    description = models.TextField(default='Description not provided.')
    catalog_version = models.CharField(max_length=512, 
        default='Version not provided.')
    
    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('department', 'number', 'title')
        ordering = ['department', 'number']

class ClassSchedule(models.Model):
    """Information about a class offered during a semester."""
    semester_code = models.PositiveIntegerField()
    semester_title = models.CharField(max_length=255)
    crn_number = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    section_number = models.PositiveIntegerField()
    max_enrollment = models.PositiveIntegerField()
    act_enrollment = models.PositiveIntegerField()
    course = models.ForeignKey(Course)
    
    def __str__(self):
        return str(self.semester_title + ' ' + str(self.course))

    class Meta:
        unique_together = ('semester_code', 'crn_number')
        ordering = ['semester_code', 'crn_number']