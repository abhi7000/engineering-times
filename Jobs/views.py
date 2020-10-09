from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializers
from .models import Job
# Create your views here.
@api_view(['GET'])
def expire(request):
	obj=Job.objects.all()
	serializer=JobSerializers(obj,many=True)
	return Response(serializer.data)