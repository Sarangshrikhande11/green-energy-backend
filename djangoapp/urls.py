from django.urls import path
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenRefreshView
from djangoapp.views import UserViewSet, CustomizedTokenObtainPairView


user_register = UserViewSet.as_view({"post": "user_register"}, permission_classes=[AllowAny])

user_myprofile = UserViewSet.as_view({"get": "myprofile"})
user_orders = UserViewSet.as_view({"get": "user_orders"})
user_appointments = UserViewSet.as_view({"get": "user_appointments"})
submitappointment = UserViewSet.as_view({"post": "submitappointment"})
completeorder = UserViewSet.as_view({"post": "completeorder"})

viewallorders = UserViewSet.as_view({"get": "viewallorders"}, permission_classes=[AllowAny])
viewallappointments = UserViewSet.as_view({"get": "viewallappointments"}, permission_classes=[AllowAny])
viewallproducts = UserViewSet.as_view({"get": "viewallproducts"}, permission_classes=[AllowAny])

addproduct = UserViewSet.as_view({"post": "addproduct"}, permission_classes=[AllowAny])
editproduct = UserViewSet.as_view({"post": "editproduct"}, permission_classes=[AllowAny])
deleteproduct = UserViewSet.as_view({"post": "deleteproduct"}, permission_classes=[AllowAny])

submitform = UserViewSet.as_view({"post": "submitform"}, permission_classes=[AllowAny])

uploadimg = UserViewSet.as_view({"post": "uploadimg"}, permission_classes=[AllowAny])

urlpatterns = [

    path("auth/login/", CustomizedTokenObtainPairView.as_view(), name="user_login"),
    path("auth/register/", user_register, name="user_register"),

    path("users/myprofile/", user_myprofile, name="user_myprofile"),
    path("users/orders/", user_orders, name="user_orders"),
    path("users/appointments/", user_appointments, name="user_appointments"),
    path("users/submitappointment/", submitappointment, name="submitappointment"),
    path("users/completeorder", completeorder, name="completeorder"),
    path("uploadimg/", uploadimg, name="uploadimg"),

    path("users/submitform/", submitform, name="submitform"),
    
    path("myadmin/viewallorders", viewallorders, name="viewallorders"),
    path("myadmin/viewallappointments", viewallappointments, name="viewallappointments"),
    path("myadmin/viewallproducts", viewallproducts, name="viewallproducts"),

    path("myadmin/addproduct", addproduct, name="addproduct"),
    path("myadmin/editproduct", editproduct, name="editproduct"),
    path("myadmin/deleteproduct", deleteproduct, name="deleteproduct"),
  
]
