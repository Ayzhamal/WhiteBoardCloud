
#view only has to be concerned with making the necessary database queries and passing that data into a template 

from django.shortcuts import render, redirect
from django.http import HttpResponse #this class build the response object that views are expected to return 
from django.http import Http404
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm

from .models import Student #import the model Student to build queries for the response page

def login_view(request):
    next=request.GET.get('next')
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    
    context={
        'form': form,
    }
    return render (request, 'login.html', context)

def register_view(request):
    next=request.GET.get('next')
    form=UserRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    
    context={
        'form': form,
    }
    return render (request, 'signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')
    

def index (request):
    return render(request, "index.html", {})

def home(request):
    students=Student.objects.all()
    return render(request, 'home.html', {'students': students})
    #return HttpResponse('<p> This is a home view</p>')

def student_detail(request, id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student not found')
    
    return render(request, 'student_detail.html', {'student': student})
    #return HttpResponse('<p>Enrollment view with the id {}</p>'.format(id))