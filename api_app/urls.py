from django.urls import path,include
from .views import VendorAPI,index,vendor
urlpatterns = [
    path("",index,name="vendor_dash"),
    path("vendor/",vendor),
    path('api/vendor',VendorAPI.as_view()),
]

