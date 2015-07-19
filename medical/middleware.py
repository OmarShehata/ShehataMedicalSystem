from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

#Helper function
from .helpers import isPatient



class AuthenticationCheckMiddleware:
	# Makes sure the app is only accessible by people logged in
	def process_request(self, request):
		if request.user.is_authenticated():#Is user is logged in, all good!
			return

		#Patients currently do not have any access to anything aside from the patient page
		if(isPatient(request.user) and request.path.find('patient') == -1):
			raise PermissionDenied;

		#Otherwise, check if this is the login page
		if(request.path.find("login") == -1):
			#If not, redirect to login
			return redirect("login")
