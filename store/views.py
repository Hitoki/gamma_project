from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Product
from django.http import Http404
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .models import Product


def store(request):
    search_query = request.GET.get('search', '')
    if search_query:
        context = {
            'products': Product.objects.filter(title__icontains=search_query)
        }
    else:
        context = {
            'products': Product.objects.all()
        }
    return render(request, 'store/store.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/store.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        product = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        category_query = self.request.GET.get('category', '')
        products = product.filter(title__icontains=search_query)
        if category_query:
            products = products.filter(category__name=category_query)
        return products


class ProductDetailView(DetailView):
    model = Product


@login_required
def add_boughted_book(request, pk):
    product = get_object_or_404(Product, pk=pk)
    profile = request.user.profile
    if not product in profile.boughted_books.all():
        profile.boughted_books.add(product)
        profile.save()
        messages.success(request, f'You successfully bought this book')
        return redirect('store')
    messages.info(request, f'You have already bought this book')
    return redirect('store')
