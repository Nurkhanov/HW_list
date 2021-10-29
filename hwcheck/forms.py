from django.forms import ModelForm
from .models import HW

class HW_input(ModelForm):

	class Meta:
		model = HW
		fields = ('hw_name','hw_info','hw_course')
		