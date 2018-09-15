from django.contrib import admin

from .models import Measurement

class MeasurementAdmin(admin.ModelAdmin):
	list_display = ['date', 'temperature', 'humidity', 'heatidx']
	list_filter = ['date']

admin.site.register(Measurement, MeasurementAdmin)
