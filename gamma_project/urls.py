"""gamma_project URL Configuration

"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('management/', include('management.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/login')),
]
