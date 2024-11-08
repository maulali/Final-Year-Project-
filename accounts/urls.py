# urls.py


# Endpoints

from django.urls import path
from .views import home_view, login_view, signup_view, contactus_view, addperson_view, dashboard_view, persondetails_view, apply_filters, get_chart_data, welcome_view, addperson_form

urlpatterns = [
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('contactus/', contactus_view, name='contactus'),
    path('addperson/', addperson_view, name='addperson'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('persondetails/', persondetails_view, name='persondetails'),
    path('apply_filters/', apply_filters, name='apply_filters'),
    path('get_chart_data/', get_chart_data, name='get_chart_data'),
    path('welcome/', welcome_view, name='welcome'),
    path('addperson_form/', addperson_form, name='addperson_form'),
]
