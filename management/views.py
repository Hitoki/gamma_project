from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . import models


# Create your views here.

class ShopListView(ListView):
    template_name = 'shop_list.html'
    queryset = models.Shop.objects.all()


class ShopDetailView(DetailView):
    template_name='shop_month.html'
    model = models.Shop


class StaffListView(ListView):
    template_name = 'staff.html'
    queryset = models.Staff.objects.all()


class StaffDetailView(DetailView):
    template_name='person.html'
    model = models.Staff
