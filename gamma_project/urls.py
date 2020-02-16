"""gamma_project URL Configuration

"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('management/', include('management.urls')),
    path('admin/', admin.site.urls),
]
