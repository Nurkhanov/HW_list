from django.forms import ModelForm,ModelChoiceField,EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import HW, Course



class HW_input(ModelForm):

	class Meta:
		model = HW
		fields = ('HW_name','HW_info','HW_course','HW_deadline')

	def __init__(self,  *args,user= None,  **kwargs,):
		super(HW_input, self).__init__(*args, **kwargs)
		self.fields['HW_deadline'].required = False
		self.fields['HW_deadline'].initial = 'dd/mm/yyyy'
		if user:
			self.fields['HW_course'].queryset = Course.objects.filter(course_user = user)
			self.fields['HW_course'].empty_label = 'Select course'

class Course_input(ModelForm):

	class Meta:
		model = Course
		fields = ('course_name',)
		
class User_input(UserCreationForm):
	email = EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1']