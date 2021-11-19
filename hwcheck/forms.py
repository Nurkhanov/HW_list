from django.forms import ModelForm
from .models import HW, Course


class HW_input(ModelForm):

	class Meta:
		model = HW
		fields = ('HW_name','HW_info','HW_course',)

class Course_input(ModelForm):

	class Meta:
		model = Course
		fields = ('course_name', 'course_id', )
		