from django.urls import path
from .views import ProductListView, ProductDetailView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='store'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/add_boughted_book/', views.add_boughted_book, name='add_boughted_book'),
]
