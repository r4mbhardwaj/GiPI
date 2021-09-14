from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from projects.models import *
import json

def get_code(request, project_name, release=None):
    try:
        rel = Release.objects.get(project__name=project_name, project__private=False)
    except:
        rel = get_object_or_404(Release, project__name=project_name, project__private=False, name=release)
    return HttpResponse(rel.file.read())
    