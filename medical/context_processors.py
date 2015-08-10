#Helper functions
from .helpers import isDoctor,isWorker,isPatient
from .models import *

def base_context_variables(request):
	#Sets variables for every page
	context = {}
	if(request.user.is_authenticated()):
		context['authenticated'] = request.user.username;
		#The state of the user
		context['isDoctor'] = isDoctor(request.user);
		context['isWorker'] = isWorker(request.user);
		context['isPatient'] = isPatient(request.user);
		#Get number of active visits
		context['visits'] = len(Visit.objects.filter(state="new"));

	return context;