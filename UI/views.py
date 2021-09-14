from django.shortcuts import render
from projects.models import *

def home(request):
    return render(request, 'UI/home.html')


def search(request):
    query = request.POST.get('query', "")
    context = {'query':query}
    if query:
        pjs = Project.objects.filter(name__icontains=query)
        context['projects'] = pjs
    return render(request, "UI/search.html", context)