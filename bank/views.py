from django.shortcuts import render
from django.http import * 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# from django.db.models import Count
from .models import *
from .forms import *


def home(request):

    if request.user.is_authenticated:
        if Hospital.objects.filter(user = request.user):
            hospitals = Hospital.objects.filter(user = request.user)
            current_hospital = Hospital.objects.filter(user = request.user)[0]
            hospital_requests = Request.objects.filter(hospital__id__in = Hospital.objects.filter(name = current_hospital.name))
            return render(request, "hospital_home.html", {"hospital_requests" : hospital_requests, "hospitals"  : hospitals})
        else:
            requests = []
            blood_details = Hospital.objects.all().order_by("name")
            if Receiver.objects.filter(user = request.user):
                receiver = Receiver.objects.get(user = request.user)
                requests = Request.objects.filter(receiver = receiver)


            if blood_details:
                page = request.GET.get('page',1)
                paginator = Paginator(blood_details, 10)
                try:
                    bloods = paginator.page(page)
                except PageNotAnInteger:
                    bloods = paginator.page(1)
                except EmptyPage:
                    bloods = paginator.page(paginator.num_pages)
                return render(request, "home.html", {"blood_details" : bloods,"requests" : requests})
            else:
                return HttpResponse("No data available")
    else:
        blood_details = Hospital.objects.all().order_by("name")
        if blood_details:   
            page = request.GET.get('page',1)
            paginator = Paginator(blood_details, 10)
            try:
                bloods = paginator.page(page)
            except PageNotAnInteger:
                bloods = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)
            context = {'blood_details' : bloods}
            return render(request,'home.html',context)
        else:
            return HttpResponse("No data available")

def hospital_registration(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        hospital_form = HospitalForm(data=request.POST)
        if user_form.is_valid() and hospital_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            hospital = hospital_form.save(commit=False)
            hospital.user = user
            if not (user_form.errors or hospital_form.errors):

                hospital.save()
            registered = True
        else:
            print(user_form.errors,hospital_form.errors)
    else:
        user_form = UserForm()
        hospital_form = HospitalForm()
    return render(request,'hospital_registration.html',
                          {'user_form':user_form,
                           'hospital_form':hospital_form,
                           'registered':registered})

def receiver_registration(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        receiver_form = ReceiverForm(data=request.POST)
        if user_form.is_valid() and receiver_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            receiver = receiver_form.save(commit=False)
            receiver.user = user
            if not (user_form.errors or receiver_form.errors):

                receiver.save()
            registered = True
        else:
            print(user_form.errors,receiver_form.errors)
    else:
        user_form = UserForm()
        receiver_form = ReceiverForm()
    return render(request,'receiver_registration.html',
                          {'user_form':user_form,
                           'receiver_form':receiver_form,
                           'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


@login_required(login_url='login')
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='login')
def add_blood_details(request):

    registered = False
    if request.method == "POST":
        blood_detail_form = BloodDetailForm(data = request.POST)
        if blood_detail_form.is_valid():
            if Hospital.objects.filter(user = request.user):
                hospitals = Hospital.objects.filter(user = request.user)
                hospital = hospitals[0]
                new_hospital = Hospital(user = request.user, name=hospital.name, street = hospital.street, city = hospital.city, pin = hospital.pin)
                blood_detail = blood_detail_form.cleaned_data.get("blood_group")
                print("bbg : ",blood_detail)
                # hospital = Hospital.objects.get(user = request.user)
                print("hospital : ",hospital.name)
                new_hospital.blood_group = blood_detail_form.cleaned_data.get("blood_group")
                new_hospital.save() 

                return HttpResponseRedirect(reverse('home'))

            else:
                    print("NO HOSPITAL FOUND WITH GIVEN USER")
                    return HttpResponse("NO HOSPITAL FOUND WITH GIVEN USER")
        else:
            return HttpResponse("Invalid Form details")
    else:
        blood_detail_form = BloodDetailForm()
        return render(request,'blood_detail_form.html',{'blood_detail_form':blood_detail_form})

@login_required(login_url='login')
def send_request(request,pk):

    done = False
    # new_receiver = Receiver.objects.get(user = request.user)
    if Receiver.objects.filter(user = request.user):
        new_receiver = Receiver.objects.get(user = request.user)
        new_hospital = Hospital.objects.get(pk = pk)
        if new_hospital.is_requested == True:
            return HttpResponse("Request already exists for this hospital and blood")
        else:
            new_hospital.is_requested = True
            new_hospital.save()
            new_request = Request(receiver = new_receiver,hospital = new_hospital)
            new_request.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse("Only receiver is authorised to request blood")