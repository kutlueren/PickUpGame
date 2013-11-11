from django.http import *
from django.core import serializers
from RestAPIWeb.models import Results
from django.views.decorators.csrf import csrf_exempt
import json as simplejson
import decimal

def get_all_result_list(request):
	data = serializers.serialize('json', Results.objects.order_by('-point'))
	#records=Results.objects.all()

	return HttpResponse(data, mimetype="application/json")
	
@csrf_exempt
def post_new_user(request):
    #data= 'Raw Data: "%s"' % request.raw_post_data  
	data=""
	HasError=False
	if request.method == 'POST':
		try:
			jsonData=simplejson.loads(request.raw_post_data)
		except:
			HasError=True
			data="exception"
	else : 
		HasError=True
		data="hata"
	
	
	for each in jsonData:
		print each['name']
		print each['point']
		obj = Results(name=each['name'], point=decimal.Decimal(each['point']))
		obj.save()
	
	
	
	data = serializers.serialize('json', Results.objects.order_by('-point'))
	return HttpResponse(data, mimetype="application/json")

# Create your views here.
