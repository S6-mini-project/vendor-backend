from django.core import serializers
from  .models import Orders,Stocks
from .serializers import OrderSerializer,StockSerializer
from django.shortcuts import  render
# Create your views here.
from rest_framework.decorators import APIView,api_view
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages
from django.db import connection


@api_view(['GET','POST'])
def index(request):
    # print(request.data)
    stocks = Stocks.objects.all()
    return render(request, "orders.html",{"stocks" : stocks})
 
@api_view(['POST','GET'])
def medicineadd(request):
    if request.method == 'GET':
            stocks = Stocks.objects.all()
            return render(request, "orders.html",{"stocks" : stocks})
    elif request.method == 'POST':
        try:
            name = request.POST.get('name')
            qty = request.POST.get('qty')
            stock_instance = Stocks.objects.create(medicine_name=name,medicine_qty=qty)
            stocks = Stocks.objects.all()
            return render(request, "orders.html",{"stocks" : stocks})
        except Exception as e:
                print(e)
        

class VendorAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self,request):
            orders = Orders.objects.all()
            print(orders)
            if request.method == 'GET':
                return render(request, "index.html",{"orders" : orders}  )
            
    def post(self,request):
        if request.method == 'POST':
            try:
                serializer = OrderSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return render(request, "index.html")       
            except Exception as e:
                print(e)

@api_view(['GET'])
def reset_id(request):
    cursor = connection.cursor()
    cursor.execute('''UPDATE `api_app_stocks` set medicine_id = (@increment_value := @increment_value+ 1) order by medicine_id''')
    stocks = Stocks.objects.all()
    return render(request, "orders.html",{"stocks" : stocks})         
    # UPDATE `api_app_stocks` set medicine_id = (@increment_value := @increment_value+ 1) order by medicine_id;

@api_view(['GET'])   
def delete_orders(request):
    cursor = connection.cursor()
    cursor.execute('''truncate table api_app_orders''') 
    orders = Orders.objects.all() 
    return render(request, "index.html",{"orders" : orders}  )       
 
@api_view(['GET'])   
def delete_stocks(request):
    cursor = connection.cursor()
    cursor.execute('''truncate table api_app_stocks''') 
    stocks = Stocks.objects.all()
    return render(request, "orders.html",{"stocks" : stocks})           
 
     
    