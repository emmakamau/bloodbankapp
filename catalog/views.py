from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from catalog.models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.core.mail import send_mail, BadHeaderError
from django.db.models.signals import post_save

# Create your views here.


def home(request):
    donors = Donor.objects.all()[:5]

    context = {
        'donors': donors,
    }
    return render (request, 'catalog/index.html', context=context)

@unauthenticated_user
def registerhosp(request):
    form = RegisterFormHosp()

    if request.method == 'POST':
        form = RegisterFormHosp(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name="Hospital")     
            user.groups.add(group)

            Hospital.objects.create(
                user=user,
                name=username,
                email=email,
                )

            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {
        'form': form,
    }
    return render (request, 'catalog/reghosp.html', context=context)


@unauthenticated_user
def registerdonor(request):
    form = RegisterFormDonor()

    if request.method == 'POST':
        form = RegisterFormDonor(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name="Donor")
            user.groups.add(group)

            Donor.objects.create(
                user=user,
                name=username,
                email=email,
                )

            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {
        'form': form,
    }
    return render (request, 'catalog/regdonor.html', context=context)


@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render (request, 'catalog/login.html', context=context)


def logoutuser(request):
    
    donors = Donor.objects.all().filter(status='Available')[:5]

    context = {
        'donors': donors,
    }
    logout(request)
    return render (request, 'catalog/index.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Hospital','Admin','Donor'])
def hospital(request):

    hospitals = Hospital.objects.all()
    
    context ={
        'hospitals': hospitals,
    }

    return render (request, 'catalog/hospital.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Hospital','Admin'])
def hospitalprofile(request, id):
    hospid = Hospital.objects.get(hospid=id)
    obj = get_object_or_404(Hospital, hospid = id) 
  
    form = HospProf(request.POST or None, instance = obj) 
  
    if form.is_valid(): 
        form.save() 
        return redirect('hospital')

    context ={
        'form': form,
    }

    return render (request, 'catalog/hospprofile.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Donor','Admin'])
def donorprofile(request, id):
    donorid = Donor.objects.get(donorid=id)
    obj = get_object_or_404(Donor, donorid = id) 
  
    form = DonorProf(request.POST or None, instance = obj) 
  
    if form.is_valid(): 
        form.save() 
        return redirect('hospital')

    context ={
        'form':form,
    }

    return render (request, 'catalog/donorprof.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Hospital','Admin'])
def donorlist(request):
    donors = Donor.objects.all().filter(status='Available')
    

    context = {
        'donors': donors,
    }
    return render(request, 'catalog/donor_list.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Hospital','Admin'])
def contacthosp(request):

    if request.method == 'GET':
        form = HospContactForm()
    else:
        form = HospContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            recipient_list = form.cleaned_data['recipient_list']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [recipient_list])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('hospital')
    
    context = {
        'form':form,
    }
    
    return render(request, 'catalog/contacthosp.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Hospital','Admin'])
def contactdonor(request):
    
    if request.method == 'GET':
        form = DonorContactForm()
    else:
        form = DonorContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            recipient_list = form.cleaned_data['recipient_list']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [recipient_list])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('hospital')
    
    context = {
        'form':form,
    }

    return render(request, 'catalog/contactdonor.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Donor','Admin'])
def scheduledonation(request):
    
    if request.method == 'GET':
        form = ScheduleDonationForm()
    else:
        form = ScheduleDonationForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            recipient_list = form.cleaned_data['recipient_list']
            subject = form.cleaned_data['subject']
            date = form.cleaned_data['date']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [recipient_list])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('hospital')
    
    context = {
        'form':form,
    }

    return render (request, 'catalog/scheduledonation.html', context=context)
