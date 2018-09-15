from django.db import models

class Measurement(models.Model):
	date = models.DateTimeField('measurement date', auto_now_add=True)
	temperature = models.FloatField(default=0)
	humidity = models.FloatField(default=0)
	heatidx = models.FloatField(default=0)
