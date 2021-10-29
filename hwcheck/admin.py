from django.contrib import admin
from django.contrib.admin.helpers import AdminField
from .models import Course,HW
# Register your models here.

admin.site.register(Course)
admin.site.register(HW)