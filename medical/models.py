from django.db import models

class patient(models.Model):
	name = models.CharField(max_length=50);
	dateofbirth = models.DateField();
	sex = models.CharField(max_length=10);
	phone = models.CharField(max_length=50);

	firstvisit = models.DateField(auto_now_add=True);
	meta = models.TextField(blank=True);

class visit(models.Model):
	patient = models.ForeignKey('patient')
	hospital = models.ForeignKey('hospital')
	hospitalID = models.CharField(max_length=50);
	referral = models.ForeignKey('referrer')
	billingPaid = models.FloatField()
	billingTotal = models.FloatField()

	#Diagnosis
	category = models.CharField(max_length=50);
	diagnosis = models.TextField(blank=True);
	followupCategory = models.CharField(max_length=50); #Cured, complicated or died
	followupInfo = models.TextField(blank=True);#If complicated, what happened? Or if died, of what?

	lastSeen = models.DateField(auto_now_add=True);

	meta = models.TextField(blank=True);

class referrer(models.Model):
	name = models.CharField(max_length=50);
	refType = models.CharField(max_length=50);#Whether it's a doctor or syndicate
	meta = models.TextField(blank=True);

class hospital(models.Model):
	name = models.CharField(max_length=50);
	address = models.CharField(max_length=200);
	meta = models.TextField(blank=True);