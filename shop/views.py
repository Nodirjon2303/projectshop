from django.shortcuts import render, redirect, Http404
from . import models
from .forms import ProductForm, ProductModelForm


def home(request):
    products = models.Product.objects.all().select_related('category')
    print(products.query)
    return render(request, 'main.html', {'products': products})


def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'add-product.html', {'form': form})


def product_detail(request, pk):
    product = models.Product.objects.filter(id=pk).first()
    # print(product.__dict__)
    if not product:
        return Http404
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('home')
    form = ProductModelForm(instance=product)
    return render(request, 'product-detail.html', {'form':form})
