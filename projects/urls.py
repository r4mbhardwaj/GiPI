from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<project_name>/', project),
    path('<project_name>/<release>', project)
]