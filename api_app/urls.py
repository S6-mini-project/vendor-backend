from django.urls import path,include
from .views import VendorAPI,index,medicineadd,delete_orders,delete_stocks,reset_id
urlpatterns = [
    path("",index,name="vendor_dash"),
    path("deleteorders/",delete_orders,name="deleteorders"),
     path("deletestocks/",delete_stocks,name="deletestocks"),
     path("medicineadd",medicineadd,name="medicineadd"),
      path("resetid/",reset_id,name="resetid"),
    path('api/vendor',VendorAPI.as_view(),name="vendor"),
]

