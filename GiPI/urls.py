from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UI.urls')),
    path('project/', include('projects.urls')),
    path('api/', include('api.urls')),
]
