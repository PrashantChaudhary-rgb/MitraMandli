from django.urls import path , include
from . import views 

urlpatterns = [
    path('',views.home, name = 'dating-home'),
    path('dashboard/',views.dashboard, name = 'dating-dashboard')

]


