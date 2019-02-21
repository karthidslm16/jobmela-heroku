from django.db import models
from user.models import job_seeker
from recruiter.models import recruiter
# Create your models here.

class job(models.Model):
	job_id = models.CharField(max_length=20, primary_key=True)
	job_name = models.CharField(max_length=30)
	job_desc = models.CharField(max_length=300)
	job_location = models.CharField(max_length=20, default='')
	job_poster = models.ForeignKey(recruiter, on_delete=models.CASCADE)
	job_req_1 = models.CharField(max_length=300, default='')
	job_req_2 = models.CharField(max_length=300, default='')
	job_req_3 = models.CharField(max_length=300, default='')
	job_req_4 = models.CharField(max_length=300, default='')

class job_application(models.Model):
	Application_Status = (
	('U', 'Unprocessed'),
	('S', 'Shortlisted'),
	('N', 'Not Shortlisted'))
	job_id = models.ForeignKey(job, on_delete=models.CASCADE)
	job_seeker_mail = models.ForeignKey(job_seeker, on_delete=models.CASCADE)
	job_app_status =  models.CharField(max_length=1, choices=Application_Status, default='U')