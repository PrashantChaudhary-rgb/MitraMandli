from django.urls import path , include
from . import views 

urlpatterns = [
    path('',views.messages_page, name = 'messages')

]