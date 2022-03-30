from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    body = request.body
    print("bodybody",body)
    data=json.loads(body)
    print(data)
    return JsonResponse({"return message":"NEW MESSAGE"})