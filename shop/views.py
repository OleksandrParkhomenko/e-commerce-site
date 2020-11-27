from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from .forms import OrderForm


def index(request):
    products = Product.objects.all()
    page_title = "Homepage"

    # search
    item_name = request.GET.get('item_name')
    if item_name != "" and item_name is not None:
        products = Product.objects.filter(title__icontains=item_name)
        page_title = "Search for '{}'".format(item_name)

    # pagination
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    if products.end_index() > 1:
        page_title += " | Page {}".format(products.number)

    context = {
        'products': products,
        'page_title': page_title
    }

    return render(request, 'shop/index.html', context)


def detail(request, id):
    object = Product.objects.get(pk=id)
    context = {
        'object': object,
        'page_title': object.title
    }
    return render(request, 'shop/detail.html', context)


@login_required
def create_product(request):
    context = {
        'page_title': 'Add new product'
    }
    return render(request, 'shop/create_product.html', context)


def checkout(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print("invalid")
    context = {
        'form': form,
        'page_title': "Checkout"
    }
    return render(request, 'shop/checkout.html', context)
