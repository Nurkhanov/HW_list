from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = 'home'),
    path('log_in/', log_in, name = 'log_in'),
    path('log_out/',log_out, name = 'log_out'),
    path('registration/', user_registration, name = 'registration'),
    path('show_hw/', show_hw, name = 'show_hw'),
    # path('change_hw/', change_hw, name = 'show_hw'),
    path('create_course/', create_course, name = 'create_course'),
]