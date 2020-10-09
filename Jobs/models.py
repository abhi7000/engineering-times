from django.db import models

# Create your models here.
class Job(models.Model):
	company_name=models.CharField(max_length=200)
	expiry_date_time=models.DateTimeField()

	def __str__(self):
		return self.company_name