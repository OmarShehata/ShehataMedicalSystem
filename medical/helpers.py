#Useful user functions
def isDoctor(user):
	return user.groups.filter(name="doctor").exists()

def isWorker(user):
	return user.groups.filter(name="worker").exists()

def isPatient(user):
	return user.groups.filter(name="patient").exists()