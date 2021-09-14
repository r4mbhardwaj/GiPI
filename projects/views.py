from django.shortcuts import render, get_object_or_404
from .models import *

def project(request, project_name, release=None):
    pj = get_object_or_404(Project, name=project_name)
    context = {'project':pj}
    if release:
        context['release'] = release
    return render(request, "projects/project.html", context)