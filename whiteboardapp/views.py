# test- Installing git
#view only has to be concerned with making the necessary database queries and passing that data into a template 

from django.shortcuts import render
from django.http import HttpResponse #this class build the response object that views are expected to return 
from django.http import Http404

from .models import Student #import the model Student to build queries for the response page

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