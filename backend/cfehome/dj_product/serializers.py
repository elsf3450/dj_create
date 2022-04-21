
#from django.forms import forms 
from rest_framework import serializers
from .models import Product

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'title','contect','price','sale_price','get_discount']