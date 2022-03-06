from email.headerregistry import Group
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import *
from .forms import *
from GFG import settings
from Geeks.decorators import admin_only, allowed_users, unauthenticated_user
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def formoo(request):
    if request.method=='POST':
        form=student(request.POST)

        username = request.POST.get('nameleader')
        useremail = request.POST.get('email')
        rollno = request.POST.get('rollno')
        send_mail(
            subject='Smart India Hackathon Registration',
            message = f'Hello {username}, {(rollno)}.\n\nThank You for registering to Smart India Hackathon. The Event will be organized on 12 March and the Problem Statements will be send to the respective registered email.\n\nStay Connected to us (cuh.gfgsc@gmail.com)',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list = [useremail],
            fail_silently=False)

        if form.is_valid():
            form.save()
            return render(request,'thankyou.html',{})
        else:
            print(form.errors)
            print('form is not valid',form)
    else:
        form=student(request.GET or None)
    return render(request,'index1.html',{'form':form})

def formoo1(request):
    if request.method=='POST':
        form=IndividualForm(request.POST)

        username = request.POST.get('name')
        useremail = request.POST.get('email')
        rollno = request.POST.get('rollno')
        send_mail(
            subject='Smart India Hackathon Registration',
            message = f'Hello Geek, {(rollno)}.\n\nThank You for registering to Smart India Hackathon. The Event will be organized on 12 March and the Problem Statements will be send to the respective registered email.\n\nStay Connected to us (cuh.gfgsc@gmail.com)',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list = [useremail],
            fail_silently=False)

        if form.is_valid():
            form.save()
            return render(request,'thankyou.html',{})
        else:
            print(form.errors)
            print('form is not valid',form)
    else:
        form=IndividualForm(request.GET or None)
    return render(request,'index.html',{'form':form})

def logoutUser(request):
    logout(request)
    return redirect('register')

def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username =username, password =password)

        if user is not None:
            login(request, user)
            return redirect('database')
        else:
            messages.info(request,"Username or Password is Incorrect!!")

    context ={}
    return render(request, 'login.html', context)

def registerPage(request):
    form = student()
    if request.method == "POST":
        form = student(request.POST)
        if form.is_valid():
            user=form.save()
            username= form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, 'Account was Successfully created for '+ username)
            return redirect('register')

    context ={'form':form}
    return render(request, 'taskapp/register.html', context)


def database(request):
    all_database = Details.objects.all()
    return render(request, 'database.html',
        {all_database: all_database})