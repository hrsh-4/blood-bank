from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

BLOOD_GROUP  = (

	("A+","A+"),
	("A-","A-"),
	("B+","B+"),
	("B-","B-"),
	("O+","O+"),
	("O-","O-"),
	("AB+","AB+"),
	("AB-","AB-")

	)

GENDER = (

	("FEMALE","FEMALE"),
	("MALE","MALE"),
	("OTHER","OTHER")

	)

class Blood(models.Model):
	blood_group = models.CharField(choices = BLOOD_GROUP,max_length= 20)

	def __str__(self):
		return self.blood_group

class Receiver(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	age =  models.PositiveIntegerField()
	gender = models.CharField(choices = GENDER,max_length = 10)
	street = models.CharField(max_length = 300)
	city = models.CharField(max_length=100)
	pin = models.PositiveIntegerField()
	blood_group = models.CharField(choices = BLOOD_GROUP, max_length =20)
	is_receiver = models.BooleanField(default = True)

	def __str__(self):
		return self.name

class Hospital(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	street = models.CharField(max_length = 300)
	city = models.CharField(max_length=100)
	pin = models.PositiveIntegerField()
	blood_group = models.ForeignKey(Blood,on_delete = models.PROTECT, blank=True,null=True)
	is_hospital = models.BooleanField(default = True)
	is_requested = models.BooleanField(default = False)

	def __str__(self):
		return self.name

	def set_request_to_true(self):
		return reverse('send-request', kwargs={
                    'pk':self.pk
        })

class Request(models.Model):
	receiver = models.ForeignKey(Receiver, on_delete = models.PROTECT)
	hospital = models.ForeignKey(Hospital, on_delete = models.PROTECT)
	date = models.DateTimeField(auto_now_add=True)
	is_approved = models.BooleanField(default = False)

	def __str__(self):
		return self.receiver.name +" to "+self.hospital.name + " for " + self.hospital.blood_group.blood_group
