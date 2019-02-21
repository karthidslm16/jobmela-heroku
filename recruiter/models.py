from django.db import models

class recruiter(models.Model):
	email = models.EmailField(max_length=30, primary_key=True)
	password = models.CharField(max_length=30)