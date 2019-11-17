from django.db import models

class Student(models.Model):
    SEX_CHOICES=[('M', 'Male'),('F', 'Female')]
    
    userame=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    student_firstname=models.CharField(max_length=100)
    student_lastname=models.CharField(max_length=100)
    student_sex=models.CharField(choices=SEX_CHOICES, max_length=1, blank=False)
    def __str__(self):
        return self.student_username
    
    courses=models.ManyToManyField('Course', blank=True)
    

class Course(models.Model):
    course_title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_title
    

# class Enrollment(models.Model):
#     student_id
#     course_id
#     enrollment_date=models.DateTimeField()
#     midterm1=models.IntegerField()
#     midterm2=models.IntegerField()
#     final=models.IntegerField()
#     grade=models.IntegerField()