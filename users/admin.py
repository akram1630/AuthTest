from django.contrib import admin
# Register your models here.
# adding models to django admin
from .models import Profile
admin.site.register(Profile)