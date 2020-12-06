from django.contrib import admin
from django.urls import path

# app_name = 'bank'
#
from bank import views

urlpatterns = [
	path("",views.home, name="home"),
	path("hospital-registration",views.hospital_registration, name="hospital-registration"),
	path("receiver-registration",views.receiver_registration,name="receiver-registraion"),
	path("login",views.user_login, name="login"),
	path("logout", views.user_logout, name="logout"),
	path("add-blood-details", views.add_blood_details, name="add-blood-details"),
	path("send-request/<int:pk>", views.send_request,name="send-request"),
]