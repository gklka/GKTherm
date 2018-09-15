from django.shortcuts import render
from django.http import HttpResponse

from .models import Measurement

def index(request):
	print(request.GET)

	if 'temp' in request.GET:
		try:
			measurement = Measurement()
			measurement.temperature = float(request.GET['temp'])

			if 'hum' in request.GET:
				measurement.humidity = float(request.GET['hum'])

			# if 'heatidx' in request.POST:
			# 	measurement.heatidx = float(request.POST['heatidx'])
			
			measurement.save()
		except Exception as e:
			print("WRONG CALL: e" % e)
	else:
		print('No temp :(')

	return HttpResponse("OK")
