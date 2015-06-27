from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def base_context_variables(request):
	#Sets variables for every page
	context = {}
	if(request.user.is_authenticated()):
		context['authenticated'] = request.user.username;

	return context;

def index(request):
	return render(request,"medical/index.html")

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