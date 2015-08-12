from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

#Helper functions
from .helpers import isDoctor,isWorker,isPatient

from .models import *

def index(request):
	# Default page for worker is create new visit page
	if(isWorker(request.user)):
		return redirect('new_patient')
	# Default page for doctor is pending visits
	if(isDoctor(request.user)):
		return redirect('pending')
	if(isPatient(request.user)):
		#Patients do not currently have permission to anything other than the patient page
		return redirect('patient');

@ensure_csrf_cookie
def new_patient(request):
	return render(request,"medical/new_patient.html")

def visit(request,ID):
	return render(request,"medical/index.html")

def visitors(request):
	context = {}
	#Get number of active visits
	context['visitList'] = Visit.objects.filter(state="new");

	return render(request,"medical/visitorList.html",context)

def pending(request):
	return render(request,"medical/index.html")

def search_page(request):
	return render(request,"medical/search.html")

def old_data(request):
	return render(request,"medical/old_data.html")

def patient(request):
	#User accounts
	return render(request,"medical/patient.html")

def login_view(request):
	#if already logged in, redirect
	if(request.user.is_authenticated()):
		return redirect("index")

	context = {}
	if(request.POST):
		#If form is submitted
		#Check if user and pass are not empty
		username = ''
		if(request.POST['username']):
			username = request.POST['username'];
		else:
			context['no_username'] = "Don't forget to enter your username!";
		password = ''
		if(request.POST['password']):
			password = request.POST['password']
		else:
			context['no_password'] = "Don't forget to enter your password!";
		if(username != '' and password != ''):
			#Attempt verification
			user = authenticate(username=username,password=password)
			if(user is not None):
				login(request,user)
				return redirect("index")
			else:
				context['incorrect'] = "Username and/or password incorrect! Make sure you entered them correctly and that your CAPS LOCK is off"

	return render(request,"medical/login.html",context)

def logout_view(request):
	#If user is already logged out
	if not request.user.is_authenticated():
		#Go to login page
		return redirect('login')

	#Otherwise log out
	logout(request)
	return render(request,"medical/logout.html")