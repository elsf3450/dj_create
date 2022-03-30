import json

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render


def api_home(request,*args,**kwargs):
    body = request.body
    print("bodybody",body)
    data=json.loads(body)

    data['headers']=request.headers
    data['content_type']=request.content_type

    print(data)
    return JsonResponse({"return message":"NEW MESSAGE"+data["WW"]})
