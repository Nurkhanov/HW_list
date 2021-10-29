from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Course(models.Model):

	course_id = models.IntegerField(primary_key=True)
	course_name = models.CharField(max_length=80)

	def __str__(self):
		return self.course_name

	class Meta:
		verbose_name = "Курсы"
		verbose_name_plural = "Курсы"

class HW(models.Model):

	#hw_id is general number of HW and hw_number is order number of hw in course

	hw_id = models.AutoField(primary_key=True)
	hw_name = models.CharField(max_length=100)
	hw_info = models.CharField(max_length=255)
	hw_status = models.BooleanField(default=False)
	hw_course = models.ForeignKey(Course,on_delete=CASCADE)

	def __str__(self):
		return self.hw_name

	class Meta:
		verbose_name = "ДЗ"
		verbose_name_plural = "ДЗ"
