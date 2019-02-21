from django.db import models

class job_seeker(models.Model):
	GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'))
	
	email = models.EmailField(max_length=30, primary_key=True)
	password = models.CharField(max_length=30)
	name = models.CharField(max_length=30, default='name')
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	age = models.SmallIntegerField(default=30)
	resume = models.CharField(max_length=300)
	phone = models.BigIntegerField(default = 1111111111)