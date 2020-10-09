from rest_framework import serializers
from .models import Job
class JobSerializers(serializers.ModelSerializer):
	class Meta:
		Model=Job
		Field={'company_name','expire_date_time'}