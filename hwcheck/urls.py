from django.urls import path
from .views import *


urlpatterns = [
    path('',home),
    path('show_hw/',show_hw),
    path('change_hw/',change_hw),
    # path('create/',CreateHW.as_view())
    #path('log_in/',log_in.AsView()),
]