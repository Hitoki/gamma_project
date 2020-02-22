from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShopListView.as_view(), name='shop-list'),
    path('staff/', views.StaffListView.as_view(), name='staff-list'),
    path('<int:pk>/', views.ShopDetailView.as_view(), name='shop-detail'),
    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff-detail'),
]
