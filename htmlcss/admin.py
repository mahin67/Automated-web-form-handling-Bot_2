from django.contrib import admin

# Register your models here.
from .models import  FIleUpload,Information

admin.site.register(FIleUpload)
admin.site.register(Information)