from django.contrib import admin
from medical.models import *

admin.site.register(patient)
admin.site.register(visit)
admin.site.register(referrer)
admin.site.register(hospital)