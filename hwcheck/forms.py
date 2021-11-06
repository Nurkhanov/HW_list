from django.forms import ModelForm
from .models import HW


class HW_input(ModelForm):

	class Meta:
		model = HW
		fields = ('HW_name','HW_info','HW_course',)
