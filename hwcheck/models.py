from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):

	course_id = models.AutoField(primary_key=True)
	course_name = models.CharField(max_length=80)
	course_user = models.ForeignKey(User, null=True, on_delete=CASCADE)

	def __str__(self):
		return self.course_name

	class Meta:
		verbose_name = "Курсы"
		verbose_name_plural = "Курсы"


class HW(models.Model):

	#hw_id is general number of HW and hw_number is order number of hw in course

	HW_id = models.AutoField(primary_key=True)
	HW_name = models.CharField(max_length=100)
	HW_user = models.ForeignKey(User,null=True, on_delete=CASCADE)
	HW_info = models.CharField(max_length=255)
	HW_status = models.BooleanField(default=False)
	HW_deadline = models.DateField(null=True)
	HW_course = models.ForeignKey(Course,on_delete=CASCADE)

	def __str__(self):
		return self.HW_name

	class Meta:
		verbose_name = "ДЗ"
		verbose_name_plural = "ДЗ"
		