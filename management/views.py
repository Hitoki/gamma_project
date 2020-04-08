import calendar
import json

from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotModified
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Sum, Count
from django.utils import timezone
from . import models


# Create your views here.

class ShopListView(ListView):
    template_name = 'shop_list.html'
    queryset = models.Shop.objects.all()


class ReportListView(ListView):
    template_name = 'report_list.html'
    queryset = models.Shop.objects.all()


class ShopDetailView(DetailView):
    template_name='shop_month.html'

    def get_queryset(self):
        now = timezone.now()
        self.day_month = calendar.monthrange(now.year, now.month)
        self.shop = get_object_or_404(models.Shop, id=self.kwargs['pk'])
        self.costs = models.Cost_type.objects.all()
        self.queryset = models.ActivityLog.objects.filter(shop=self.shop, date__month=now.month).values('date', 'cost__cost_type', 'amount')
        return self.queryset
    
    def aggregate_data(self):
        self.data = {}
        count_cost = self.costs.aggregate(Count('id'))
        for i in range(count_cost['id__count']):
            name = self.costs.filter(id=i+1).values('name')
            self.data[i+1] = {'name': name[0]['name'], 'days': {}}
            for j in range(self.day_month[1]):
                self.data[i+1]['days'][j+1] = self.queryset.filter(date__day=j+1, cost__cost_type=i+1).aggregate(Sum('amount'))
        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = self.shop
        context['data'] = self.aggregate_data()
        return context

class StaffListView(ListView):
    template_name = 'staff.html'
    queryset = models.Staff.objects.all()


class StaffDetailView(DetailView):
    template_name='person.html'
    model = models.Staff


class ActivityDetailView(DetailView):
    template_name='report.html'

    def get_queryset(self):
        self.day = datetime.today()
        self.shop = get_object_or_404(models.Shop, id=self.kwargs['pk'])
        self.queryset = models.ActivityLog.objects.filter(shop=self.shop).all()
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = self.shop
        context['cost'] = models.Cost_type.objects.all()
        context['staff'] = models.Staff.objects.all()
        context['day'] = self.day
        context['begin_cash'] = self.queryset.filter(date=self.day-timedelta(days=1), cost=6).values('amount')
        return context


class ManagementAPIView(View):
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.POST.get('content'))
        for row in data:
            models.ActivityLog(
                date = datetime.strptime(row['day'],'%Y-%m-%d').date(),
                shop_id = int(row['shop']),
                cost_id = int(row['cost']),
                amount = float(row['amount']),
                staff_member_id = int(row['staff']),
            ).save()
        return HttpResponseNotModified()
