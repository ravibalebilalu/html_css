"""
URL configuration for html_css_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from notes.views import my_view,students_list,edit_student

urlpatterns = [
    path('',my_view,name="my_view"),
    path('students_list/',students_list,name='students_list'),
    path('edit_student/<id>/',edit_student,name = 'edit_student'),
    path('admin/', admin.site.urls),
]
