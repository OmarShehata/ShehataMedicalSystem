from django.contrib import admin
from medical.models import *

admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Referrer)
admin.site.register(Hospital)