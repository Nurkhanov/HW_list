from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = 'home'),
    path('show_hw/', show_hw, name = 'show_hw'),
    # path('change_hw/', change_hw, name = 'show_hw'),
    path('log_in/', log_in, name = 'log_in'),
    path('registration/', user_registration, name = 'registration')
]