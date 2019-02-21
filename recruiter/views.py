from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound
from .models import recruiter
from jobs.models import job, job_application
from user.models import job_seeker
from django.core.mail import *

def show(request):
	if(request.session.has_key('recruiter_account')):
		print("has account")
		user = recruiter.objects.filter(email = request.session['recruiter_account']).first()
		mess = job.objects.filter(job_poster = user)
		return render(request, 'recruiter.html', {"user":user,"message":mess, "app_status":"On the home page"})
	else:
		print("has not account")
		return render(request, 'recruiter_login.html', {"message":"Login to Apply"})

def login(request):
    return render(request, 'recruiter_login.html',{"message":""})

def logout(request):
	del request.session['recruiter_account']
	return render(request, 'home.html',{"message":""})

def register(request):
    return render(request, 'recruiter_register.html',{"message":""})  

def logining(request):
	if(request.session.has_key('recruiter_account')):
		user = recruiter.objects.filter(email = request.session['recruiter_account']).first()
		mess = job.objects.filter(job_poster = user)
		return render(request, 'recruiter.html',{ "user":user,"message":mess,"app_status":"On the home page"})

	mail = request.POST.get("email")
	pswd = request.POST.get("pwd")
	record = recruiter.objects.filter(email = mail).first()
	message = ""
	if(mail == "" or pswd == ""):
		print("enter required fields")
		message = "Enter required fields"
	elif (record):
		if (record.password == pswd):
			print("Loggining SuccessFully")
			request.session['recruiter_account'] = mail
			user = recruiter.objects.filter(email =request.session['recruiter_account']).first()
			mess = job.objects.filter(job_poster = user)
			return render(request, 'recruiter.html',{"user":user, "message":mess,"app_status":"Logged in SuccessFully"})
		else:
			print("Password doesn't match")
			message = "Password doesn't match"
	else:
		print("not registered")
		message = "Account doesn't registered"
	return render(request, 'recruiter_login.html', {"message":message})

def registering(request):
	mail = request.POST.get("email")
	pswd1 = request.POST.get("pwd1")
	pswd2 = request.POST.get("pwd2")
	strg = ""
	nature = ""
	if(mail == "" or pswd1 == "" or pswd2 == ""):
		print( "fields are null")
		strg = "Fields should not be null"
		nature = "red"
	elif(pswd2!=pswd1):
		print("password doesn't match")
		strg = "Password doesn't match"
		nature = "red"
	elif(recruiter.objects.filter(email = mail)):
		print("Record already exits")
		strg = "Record already exits"
		nature = "red"
	else:
		p = recruiter(email = mail, password = pswd1)
		p.save()
		print("SuccessFully registered.")
		strg = "SuccessFully Registered"
		nature = "lime"
	return render(request, 'recruiter_register.html',{"message":strg, "nature":nature})

def createjob(request):
	if(request.session.has_key('recruiter_account')):
		print("has account")
		user = recruiter.objects.filter(email = request.session['recruiter_account']).first()
		return render(request, 'register_job.html', {"user":user,"message":""})
	else:
		print("has not account")
		return render(request, 'recruiter_login.html', {"message":"Login to Apply"})

def deletejob(request, Job_id):
	if(request.session.has_key('recruiter_account')):
		print("has account")
		job_appl = job_application.objects.filter(job_id = Job_id)
		for x in job_appl:
			x.delete()
		Job = job.objects.filter(job_id = Job_id).first()
		Job.delete()
		Job_poster = recruiter.objects.filter(email = request.session['recruiter_account']).first()
		mess = job.objects.filter(job_poster = Job_poster)
		return render(request, 'recruiter.html', {"user":Job_poster,"message":mess, "app_status":"Job Deleted SuccessFully."})
	else:
		print("has not account")
		return render(request, 'recruiter_login.html', {"message":"Login to Apply"})

def registeringjob(request):
	if(request.session.has_key('recruiter_account')):
		Job_id = request.POST.get("job_id")
		Job_name = request.POST.get("job_name")
		Job_desc = request.POST.get("job_desc")
		Job_location = request.POST.get("job_location")
		Job_poster = recruiter.objects.filter(email = request.session['recruiter_account']).first()
		Job_req_1 = request.POST.get("job_req_1")
		Job_req_2 = request.POST.get("job_req_2")
		Job_req_3 = request.POST.get("job_req_3")
		Job_req_4 = request.POST.get("job_req_4")

		if(Job_id == "" or Job_name == "" or Job_desc == "" or Job_location == "" or Job_req_1 == "" or Job_req_2 == "" or Job_req_3 == "" or Job_req_4 == ""):
			print( "fields are null")
			strg = "Fields should not be null"
			nature = "red"
			return render(request, 'recruiter_job.html',{"message":strg,"nature":nature})
		else:
			p = job()
			p.job_id = Job_id
			p.job_name = Job_name
			p.job_desc = Job_desc
			p.job_location = Job_location
			p.job_poster = Job_poster
			p.job_req_1 = Job_req_1
			p.job_req_2 = Job_req_2
			p.job_req_3 = Job_req_3
			p.job_req_4 = Job_req_4
			p.save()
			print("SuccessFully registered.")
			mess = job.objects.filter(job_poster = Job_poster)
		return render(request, 'recruiter.html',{"user":Job_poster,"message":mess, "app_status":"Job SuccessFully Created."})
	else:
		return render(request, 'recruiter_login.html', {"message":"Login to Apply"})

def selectcandidate(request, Job_id):
	if(request.session.has_key('recruiter_account')):
		user = recruiter.objects.filter(email = request.session['recruiter_account']).first()
		mess = job_application.objects.filter(job_id = Job_id, job_app_status = 'U').values('job_seeker_mail')
		message = []
		print("debug 1")
		for mes in mess:
			print(mes)
			message.append(job_seeker.objects.filter(email = mes['job_seeker_mail']).first())
		return render(request, 'recruiter_selection.html', {"user":user, "message":message, "Job_id": Job_id})
	else:
		return render(request, 'recruiter_login.html', {"message":"Login to Apply"})

def shortlist(request, Job_seeker_mail, Job_id):
	if(request.session.has_key('recruiter_account')):
		jobb = job_application.objects.filter(job_id = Job_id, job_seeker_mail = Job_seeker_mail).first()
		if(request.POST.get("Rel_exp") or request.POST.get("Ovr_exp") or request.POST.get("Rel_skill")
			or request.POST.get("Irrelavant") ):
			jobb.job_app_status = 'N'
		else:
			jobb.job_app_status = 'S'

		jobb.save()

		reason = []
		if(request.POST.get("Rel_exp")):
			reason.append(request.POST.get("Rel_exp"));
		if(request.POST.get("Ovr_exp")):
			reason.append(request.POST.get("Ovr_exp"));
		if(request.POST.get("Rel_skill")):
			reason.append(request.POST.get("Rel_skill"));
		if(request.POST.get("Irrelavant")):
			reason.append(request.POST.get("Irrelavant"));

		post_mail(request.session['recruiter_account'], jobb.job_app_status, reason, Job_seeker_mail)
		user = recruiter.objects.filter(email = request.session['recruiter_account']).first()
		mess = job_application.objects.filter(job_id = Job_id, job_app_status = 'U').values('job_seeker_mail')

		message = []
		for mes in mess:
			message.append(job_seeker.objects.filter(email = mes['job_seeker_mail']).first())

		return render(request, 'recruiter_selection.html', {"user":user, "message": message, "Job_id":Job_id})
	else:
		return render(request, 'recruiter_login.html', {"message":"Login to Apply"})

def post_mail(frm, status, reason, too):

	usr = frm
	pswd = recruiter.objects.get(email = frm).password
	print(pswd)
	body1 = "You are "
	body2 = ""
	if(status == 'N'):
		body2 = "not" 
	body3 = "shortlisted for the Further processing\n"
	body4 = ""
	if(status == 'N'):
		body4 = "Reason for not Shortlisting:\n"
		for rea in reason:
			body4 += rea + '\n'

	Body = body1 + body2 + body3 + body4
	send_mail(subject = 'Regarding the status of Job application (JobMela)', message = Body, from_email = frm, recipient_list = [too], auth_user=usr, auth_password=pswd,
		fail_silently=False)