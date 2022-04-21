import json
from pyexpat import model

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render

from dj_product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dj_product.serializers import ProductSerialize 
@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):
    instance=Product.objects.all()[0]
    data = ProductSerialize(instance).data
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
    '''
    body = request.body
    print('bodybodybody0,body',body)
    print("request.headers",request.GET)
    model_data=Product.objects.all().order_by("?").first()
    data = {}
    '''
    '''
    data['id']=model_data.id
    data["title"] = model_data.title
    data["content"] = model_data.contect
    data["price"] = model_data.price
    '''
    #data=model_to_dict(model_data,fields=['id','title','price','sale_price'])
    return Response(data)
    #return Response(data,status=405)
    #return JsonResponse({"return message":"NEW MESSAGE"+data["WW"]})
