import json
from pyexpat import model

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render

from dj_product.models import Product

def api_home(request,*args,**kwargs):
    '''
    body = request.body
    print("bodybody",body)
    data=json.loads(body)

    data['headers']=request.headers
    data['content_type']=request.content_type
    data['params']=request.GET
    print("request.GET",request.GET)
    print("A_A",type(json.dumps(dict(request.headers))))
    print(data)
    '''
    model_data=Product.objects.all().order_by("?").first()
    data = {}
    data["title"] = model_data.title
    data["content"] = model_data.contect
    data["price"] = model_data.price
    return JsonResponse(data)
    #return JsonResponse({"return message":"NEW MESSAGE"+data["WW"]})
