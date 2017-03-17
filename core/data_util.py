# data_util.py

from courses.models import Course, ClassSchedule
import os, csv

from django.db import IntegrityError


"""A set of utility functions for loading and manipulating csv data
files. 

2017-02-23 csv header:
(TERM_CODE,TERM_DESCRIPTION,CRN,SUBJECT,COURSE_NUMBER,SECTION,SCHEDULE_DESC,TITLE,MAXIMUM_ENROLLMENT,ACTUAL_ENROLLMENT)

Example:
(200610,Fall Semester 2005,2509,CS,101,001,Lecture,Living with Computers,40,39)
"""

def csv_to_json(path=None):
	"""Makes system call to csvjson. csvkit package required on system."""

	cname = os.path.basename(path)
	jname = os.path.join(cname[:-4] + '.json')
	cmd = 'csvjson --no-inference -i 2 ' + cname + ' > ' + jname
	os.system(cmd)
	print cmd, '\nwrote', jname


def load_schedule_data_json(path=None, fake=False):
	with open(path, "r") as data_open:
		data_open_json = json.loads(data_open.read())
		for item in data_open_json:
            try:
                course_obj = Course.objects.get(department=item['SUBJECT'], number=item['COURSE_NUMBER'], title=item['TITLE'])
            except Course.DoesNotExist:
                course_obj = Course(
                    department=item['SUBJECT'], 
                    number=item['COURSE_NUMBER'], 
                    title=item['TITLE']
                )
                course_obj.save()

			try:
                class_schedule = ClassSchedule.objects.get(
                    semester_code=item['TERM_CODE'],
                    crn_number=item['CRN']
                )
			except ClassSchedule.DoesNotExist:  
                class_schedule = ClassSchedule()
                class_schedule.course = course_obj
                class_schedule.semester_code = item['TERM_CODE']
                class_schedule.semester_title = item['TERM_DESCRIPTION']
                class_schedule.crn_number = item['CRN']
                class_schedule.description = item['SCHEDULE_DESC']
                class_schedule.section_number = item['SECTION']
                class_schedule.max_enrollment = item['MAXIMUM_ENROLLMENT']
                class_schedule.act_enrollment = item['ACTUAL_ENROLLMENT']
                class_schedule.save()

def load_schedule_data_csv(path=None):
    """import data in django shell:
        
        from core.data_util import load_schedule_data_csv
        p = './core/data/cs-enrollment-f2005-s2017-report-2017-feb-22.csv'
        load_schedule_data(p)
    """

    with open(path, "r") as data_open:
        #read the file using csv reader module.
        data_open_csv = csv.reader(data_open)
        #skip the first row of the CSV file.
        next(data_open_csv)
        for row in data_open_csv:
            try:
                course_obj = Course.objects.get(department=row[3], number=row[4], title=row[7])
                
            except Course.DoesNotExist:
                course_obj = Course(department=row[3], number=row[4], title=row[7])
                course_obj.save()

            try:
                schedule_obj = ClassSchedule.objects.get(semester_code=row[0],crn_number=row[2])
                    
            except ClassSchedule.DoesNotExist:            
                schedule_obj = ClassSchedule(
                    course = course_obj,
                    semester_code = row[0],
                    semester_title = row[1],
                    crn_number = row[2],
                    description = row[6],
                    section_number = row[5],
                    max_enrollment = row[8],
                    act_enrollment = row[9]
                )
                schedule_obj.save()


if __name__ == '__main__':
	csv_to_json('PATH TO CSV DATA FILE')



		
