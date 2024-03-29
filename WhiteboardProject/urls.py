"""WhiteboardProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path #python3.7 uses re_path instead of path to use regular expressions
from whiteboardapp import views 
from django.conf.urls import url

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index, name="index"),
    re_path(r'^student/(\d+)', views.student_detail, name="student_detail"),
    re_path(r'accounts/login/', views.login_view), 
    re_path(r'accounts/register/', views.register_view),
    re_path('accounts/logout/', views.logout_view)
]
