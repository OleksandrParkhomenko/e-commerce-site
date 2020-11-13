from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from .forms import OrderForm


def index(request):
    products = Product.objects.all()

    # search
    item_name = request.GET.get('item_name')
    if item_name != "" and item_name is not None:
        products = Product.objects.filter(title__icontains=item_name)

    # pagination
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


def detail(request, id):
    object = Product.objects.get(pk=id)
    context = {
        'object': object,
    }
    return render(request, 'shop/detail.html', context)


def checkout(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print("invalid")
    context = {
        'form': form,
    }
    return render(request, 'shop/checkout.html', context)
