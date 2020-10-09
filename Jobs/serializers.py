from rest_framework import serializers
from .models import Job
class JobSerializers(serializers.ModelSerializer):
	class Meta:
		model=Job
		fields=['company_name','expiry_date_time']