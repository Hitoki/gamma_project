from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShopListView.as_view(), name='shop-list'),
    path('<int:pk>/<int:month_delta>/', views.ShopDetailView.as_view(), name='shop-detail'),
    path('staff/', views.StaffListView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff-detail'),
    path('report/', views.ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/', views.ActivityDetailView.as_view(), name='activity-detail'),
    path('api/', views.ManagementAPIView.as_view(), name='management-api'),
]
