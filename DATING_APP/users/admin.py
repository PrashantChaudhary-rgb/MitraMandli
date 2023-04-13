from django.contrib import admin
from .models import UserProfile
from .models import CustomUser



admin.site.register(CustomUser)

admin.site.register(UserProfile)
