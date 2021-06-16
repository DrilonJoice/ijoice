from django.db import models

#Online student financial assistance

class Applicant(models.Model):
	fname = models.TextField(default="")
	fschool = models.TextField(default="")
	
	class meta:
		db_table = "iApplicant"
	
class Student_Information(models.Model):
	ggrade_year = models.TextField(default="")
	gaddress = models.TextField(default="")
	gcontactno = models.IntegerField(default="")
	applicant = models.ForeignKey(Applicant, default=None, on_delete=models.PROTECT)

	class meta:
		db_table = "iStudent_information"

class School_Record(models.Model):
	hcor = models.TextField(default="")
	htor = models.TextField(default="")
	student_Information = models.ForeignKey(Student_Information, default=None, on_delete=models.PROTECT)


	class meta:
		db_table = "iSchool_record"

class Scholarship(models.Model):
	icategory = models.TextField(default="")
	itype = models.TextField(default="")
	school_Record = models.ForeignKey(School_Record, default=None, on_delete=models.PROTECT)

	class meta:
		db_table = "iScholarship"

class Status(models.Model):
	jstatus = models.TextField(default="")
	jremarks = models.TextField(default="")
	jdate = models.DateTimeField(default="")
	scholarship = models.ForeignKey(Scholarship, default=None, on_delete=models.PROTECT)

	class meta:
		db_table = "iStatus"
