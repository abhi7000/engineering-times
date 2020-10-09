from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializers
from .models import Job
import datetime

# Create your views here.
@api_view(['GET'])
def expire(request):
	obj=Job.objects.filter(expiry_date_time__date__gt=datetime.date(2020, 10, 10))
	serializer=JobSerializers(obj,many=True)
	return Response(serializer.data)