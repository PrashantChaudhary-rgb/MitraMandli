from django.contrib import admin
from django.urls import path , include
from users import views as userViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',include('dating.urls')),
    path('admin/', admin.site.urls),
    path('register/', userViews.register , name = 'register'),
    path('register/create-profile', userViews.createProfile , name = 'create-profile'),
    path('login/', auth_views.LoginView.as_view( template_name = 'users\login.html') , name = 'login'),
    path('logout/', auth_views.LogoutView.as_view( template_name = 'users\logout.html') , name = 'logout'),
    

]
