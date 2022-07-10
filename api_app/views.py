from django.core import serializers
from  .models import Orders
from .serializers import OrderSerializer
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from rest_framework.decorators import APIView,api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.forms.models import model_to_dict

@api_view(['GET','POST'])
def index(request):
    
            # return render(request,"orders.html")
            return render(request, "index.html")
    #  elif request.method == 'POST':
    #         # print(type,request.data['qty'])
    #         qty = str(request.data['qty'])
    #         context={
    #              "data" : "User has ordered "+qty+" Paracetamol",
    #         }
    #         print(context["data"])
    #         # val = context["data"]
    #         return render(request, "orders.html")

@api_view(['GET'])
def vendor(request):
    if request.method == 'GET':
            # print(type,request.data['qty'])
            # if request.method == 'GET':
            #     qty = str(request.GET.get('qty'))
            #     # print(request.GET)
            #     print(qty)
            #     context={
            #         "data" : "User has ordered "+qty+" Paracetamol",
            #     }
            return render(request, "orders.html")
    # elif request.method == 'GET':
    #         # qty = str(request.data['qty'])
    #         # print(request.data)
    #         return render(request,"orders.html")  
   
class VendorAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self,request):
            orders = Orders.objects.all()
            serializer = OrderSerializer(orders, many=True)
            # values = serializers.serialize( "python", Orders.objects.all() )
            print(serializer.data[0]['qty'])
            if request.method == 'GET':
                # context = {
                #         "data" : "User has ordered "+serializer.data[0]['qty']+" nos Paracetamol"
                #         # "data" : serializer.data
                #     }
                return render(request, "index.html",{"orders" : orders}  )
            
    def post(self,request):
                # print(type,request.data['qty'])
            #  print(request.data['qty'])
            #  qty=request.data['qty']
        if request.method == 'POST':
            try:
                serializer = OrderSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return render(request, "orders.html")       
            except Exception as e:
                print(e)
                # return HttpResponse(data)
            # return render(request, "orders.html",context)    