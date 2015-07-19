from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
import datetime

from .models import *
import json;

def searchPatients(request):
	#Recieves post data of a search term
	#Returns patients found for that term 
	if(not 'search' in request.POST):
		raise Http404
	#Search for patients by name 
	print(request.POST['search'])
	patientResults = Patient.objects.filter(name__icontains=request.POST['search']);
	patientArray = [];
	for p in patientResults:
		pObj = {}
		pObj['name'] = p.name;
		patientArray.append(pObj)

	return JsonResponse(patientArray,safe=False)

def createPatient(request):
	#Recieves post data of patient information
	#Creates new record. Returns "success" if all goes well

	patient = Patient();
	patient.name = request.POST['fullname']
	datejson = json.loads(request.POST['date_of_birth']);

	patient.dateofbirth = datetime.date(year=datejson['year'],month=datejson['month'],day=datejson['day']);
	if('male' in request.POST):
		patient.sex = "male"
	else:
		patient.sex = "female"
	patient.phone = request.POST['phonenumber']
	patient.save();

	return HttpResponse("success");