from django.http import *
from django.core import serializers
from RestAPIWeb.models import Results

def get_all_result_list(request):
	data = serializers.serialize('json', Results.objects.order_by('-point'))
	#records=Results.objects.all()

	return HttpResponse(data, mimetype="application/json")

# Create your views here.
