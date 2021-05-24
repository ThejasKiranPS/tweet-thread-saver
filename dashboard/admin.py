from django.contrib import admin
from .models import Thread, DeletedThread

# Register your models here.
admin.site.register(Thread)
admin.site.register(DeletedThread)