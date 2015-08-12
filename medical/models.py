from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length=50);
	dateofbirth = models.DateField();
	sex = models.CharField(max_length=10);
	phone = models.CharField(max_length=50);

	firstvisit = models.DateField(auto_now_add=True);
	meta = models.TextField(blank=True);
	def __str__(self):
		return self.name;

class Visit(models.Model):
	state = models.CharField(default="new",max_length=50);#new, pending, or complete

	patient = models.ForeignKey('Patient')
	hospital = models.ForeignKey('Hospital',null=True)
	hospitalID = models.CharField(default=-1,max_length=50);
	referral = models.ForeignKey('Referrer',null=True)
	billingPaid = models.FloatField(default=0)
	billingTotal = models.FloatField(default=1)

	#Diagnosis
	category = models.CharField(blank=True,max_length=50);
	diagnosis = models.TextField(blank=True);
	followupCategory = models.CharField(blank=True,max_length=50); #Cured, complicated or died
	followupInfo = models.TextField(blank=True);#If complicated, what happened? Or if died, of what?

	lastSeen = models.DateField(auto_now=True);
	createdTime =  models.DateTimeField(auto_now_add=True);

	meta = models.TextField(blank=True);

	def __str__(self):
		return self.patient.name + " - " + str(self.lastSeen);

class Referrer(models.Model):
	name = models.CharField(max_length=50);
	refType = models.CharField(max_length=50);#Whether it's a doctor or syndicate
	meta = models.TextField(blank=True);

class Hospital(models.Model):
	name = models.CharField(max_length=50);
	address = models.CharField(max_length=200);
	meta = models.TextField(blank=True);