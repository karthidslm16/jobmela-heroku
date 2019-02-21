from django.contrib import admin

# Register your models here.
from .models import job_application,job

admin.site.register(job_application)
admin.site.register(job)
