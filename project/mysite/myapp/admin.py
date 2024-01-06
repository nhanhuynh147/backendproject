from django.contrib import admin
from .models import Voltage,Current,Power,test

# Register your models here.
admin.site.register(Voltage)
admin.site.register(Current)
admin.site.register(Power)
admin.site.register(test)