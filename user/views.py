from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound
from .models import job_seeker
from jobs.models import job, job_application


def show(request):
	if(request.session.has_key('user_account')):
		mess = job.objects.all()
		user = job_seeker.objects.filter(email = request.session['user_account']).first()
		return render(request, 'user.html',{ "user":user,"message":mess,"app_status":"On the home page"})
	else:
		return render(request, 'user_login.html',{"message":"Login to Apply"})

def login(request):
   return render(request, 'user_login.html',{"message":""})

def logout(request):
	del request.session['user_account']
	return render(request, 'home.html',{"message":""})

def register(request):
	return render(request, 'user_register.html',{"message":""})

def apply(request, Job_id):
	if(request.session.has_key('user_account')):
		status = ""
		mail = request.session['user_account']
		job_seker = job_seeker.objects.filter(email = mail).first()
		jobs = job.objects.filter(job_id = Job_id).first()
		job_ap = job_application.objects.filter(job_seeker_mail = job_seker, job_id = jobs).first()
		if(job_ap):
			status = "Already Applied"
		else:
			status = "Applied SuccessFully"
			apl = job_application(job_seeker_mail = job_seker, job_id = jobs)
			apl.save()
		user = job_seeker.objects.filter(email = request.session['user_account']).first()
		message = job.objects.all()
		return render(request, 'user.html',{"user":user, "message":message, "app_status":status})
	else:
		return render(request, 'user_login.html', {"message":"Login to Apply"})

def search(request):
	if(request.session.has_key('user_account')):
		key = request.GET.get("search_word")
		mess1 = job.objects.filter(job_req_1__contains = key)
		mess2 = job.objects.filter(job_req_2__contains = key)
		mess3 = job.objects.filter(job_req_3__contains = key)
		mess4 = job.objects.filter(job_req_4__contains = key)
		mess5 = job.objects.filter(job_location__contains = key)
		mess6 = job.objects.filter(job_id__contains = key)
		mess7 = job.objects.filter(job_name__contains = key)

		mess = mess1.union(mess2, mess3, mess4, mess5, mess6, mess7)

		user = job_seeker.objects.filter(email = request.session['user_account']).first()
		print(mess)
		if mess.exists():
			app_status = "Search Result found"
		else:
			app_status = "No Search results found"
		return render(request, 'user.html',{ "user":user, "message":mess, "app_status":app_status})
	else:
		return render(request, 'user_login.html', {"message":"Login to Apply"})

def logining(request):

	if(request.session.has_key('user_account')):
		mess = job.objects.all()
		user = job_seeker.objects.filter(email = request.session['user_account']).first()
		return render(request, 'user.html',{ "user":user,"message":mess,"app_status":"On the home page"})

	mail = request.POST.get("email")
	pswd = request.POST.get("pwd")
	record = job_seeker.objects.filter(email = mail).first()
	message = ""
	if(mail == "" or pswd == ""):
		print("enter required fields")
		message = "Enter required fields"
	elif (record):
		if (record.password == pswd):
			print("Loggining SuccessFully")
			request.session['user_account'] = mail
			user = job_seeker.objects.filter(email =request.session['user_account']).first()
			mess = job.objects.all()
			return render(request, 'user.html',{"user":user, "message":mess,"app_status":"Logged in SuccessFully"})
		else:
			print("Password doesn't match")
			message = "Password doesn't match"
	else:
		print("not registered")
		message = "Account doesn't registered"
	return render(request, 'user_login.html', {"message":message})

def registering(request):
	mail = request.POST.get("email")
	pswd1 = request.POST.get("pwd1")
	pswd2 = request.POST.get("pwd2")
	strg = ""
	nature = ""
	if(mail == "" or pswd1 == "" or pswd2 == ""):
		print( "fields are null")
		strg = "fields should not be null"
		nature = "red"
	elif(pswd2!=pswd1):
		print("password doesn't match")
		strg = "password doesn't match"
		nature = "red"
	elif(job_seeker.objects.filter(email = mail)):
		print("Record already exits")
		strg = "Record already exits"
		nature = "red"
	else:
		p = job_seeker(email = mail, password = pswd1)
		p.save()
		print("SuccessFully registered.")
		strg = "SuccessFully Registered"
		nature = "lime"
	return render(request, 'user_register.html',{"message":strg, "nature":nature})

def update_profile(request):
	if(request.session.has_key('user_account')):
		key = request.session['user_account']
		obj = job_seeker.objects.filter(email = key).first()
		obj.name = request.POST.get("name")
		obj.gender = request.POST.get("gender")
		obj.age = request.POST.get("age")
		obj.resume = request.POST. get("resume")
		obj.phone = request.POST.get("phone")
		obj.save()
		return render(request, 'user.html', { "user":obj,"message":mess,"app_status":"On the home page"} )
	else:
		return render(request, 'user_login.html', {"message":"Login to Apply"})