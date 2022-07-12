from rest_framework import serializers
from .models import Orders,Stocks

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        exclude = ('o_id','created_at','updated_at')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        exclude = ['medicine_id']        