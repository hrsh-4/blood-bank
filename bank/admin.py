from django.contrib import admin

# Register your models here.
 
from .models import Blood, Hospital, Receiver, Request

admin.site.register(Blood)
admin.site.register(Hospital)
admin.site.register(Receiver)
admin.site.register(Request)