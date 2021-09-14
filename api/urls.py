from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<project_name>/<release>', get_code)
]