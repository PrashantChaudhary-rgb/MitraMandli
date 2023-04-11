from django.urls import path , include
from . import views 

urlpatterns = [
    path('',views.home, name = 'dating_home')

]


