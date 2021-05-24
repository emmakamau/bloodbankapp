from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Hospital)
admin.site.register(Donor)
admin.site.register(BloodGroup)
admin.site.register(Location)



