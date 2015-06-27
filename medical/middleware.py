from django.shortcuts import render, redirect

class AuthenticationCheckMiddleware:
	# Makes sure the app is only accessible by people logged in
	def process_request(self, request):
		if request.user.is_authenticated():#Is user is logged in, all good!
			return

		#Otherwise, check if this is the login page
		if(request.path.find("login") == -1):
			#If not, redirect to login
			return redirect("login")
