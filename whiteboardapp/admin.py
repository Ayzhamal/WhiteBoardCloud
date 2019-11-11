from django.contrib import admin

from .models import Student
from .models import Course

@admin.register(Student, Course)
class Admin(admin.ModelAdmin):
    pass
    # list_display=['student_name']