import calendar
import json

from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotModified
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from django.http import Http404

from . import models


# Create your views here.

class ShopListView(LoginRequiredMixin, ListView):
    template_name = 'shop_list.html'
    queryset = models.Shop.objects.all()


class ReportListView(LoginRequiredMixin, ListView):
    template_name = 'report_list.html'
    queryset = models.Shop.objects.all()


class ShopDetailView(LoginRequiredMixin, DetailView):
    template_name='shop_month.html'

    def date_manipulation(self, month_delta):
        today = datetime.today()
        year = today.year
        month = today.month - month_delta or 12
        now = {'year': year, 'month': month}
        return now

    def get_queryset(self, request):
        self.month_delta = self.kwargs['month_delta']
        self.now = self.date_manipulation(self.month_delta)
        self.shop = get_object_or_404(models.Shop, id=self.kwargs['pk'])
        self.queryset = models.ActivityLog.objects.filter(shop_id=self.shop, date__month=self.now['month']).values('date', 'cost__cost_type', 'amount')
        return self.queryset

    def get_object(self, request, queryset=None):
        queryset = self.get_queryset(request)
        try:
            obj = queryset[0]
        except IndexError:
            raise Http404("Data is empty")
        return obj
    
    def aggregate_data(self):
        self.data = {}
        count_cost = self.costs.aggregate(Count('id'))
        for i in range(count_cost['id__count']):
            name = self.costs.filter(id=i+1).values('name')
            self.data[i+1] = {'name': name[0]['name'], 'days': {}}
            day_month = calendar.monthrange(self.now['year'], self.now['month'])
            for j in range(day_month[1]):
                self.data[i+1]['days'][j+1] = self.queryset.filter(cost__cost_type=i+1, date__day=j+1).aggregate(Sum('amount'))
        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = self.shop
        self.costs = models.Cost_type.objects.all()
        month_list = ['Январь', 'Февраль', 'Март',
                      'Апрель', 'Май', 'Июнь',
                      'Июль','Август', 'Сентябрь',
                      'Октябрь', 'Ноябрь', 'Декабрь']
        context['month'] = month_list[self.now['month']-1]
        context['month_delta'] = self.month_delta
        context['data'] = self.aggregate_data()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(request)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class StaffListView(LoginRequiredMixin, ListView):
    template_name = 'staff.html'
    queryset = models.Staff.objects.all()


class StaffDetailView(LoginRequiredMixin, DetailView):
    template_name='person.html'
    model = models.Staff


class ActivityDetailView(LoginRequiredMixin, DetailView):
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
                shop = models.Shop.objects.get(id=int(row['shop'])),
                cost = models.Cost.objects.get(id=int(row['cost'])),
                amount = float(row['amount']),
                staff_member = models.Staff.objects.get(id=int(row['staff'])),
            ).save()
        return HttpResponseNotModified()
