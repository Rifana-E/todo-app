from django.shortcuts import render, redirect, get_object_or_404
from shoppingcart.models import Category, Product, ShoppedItemList
from django.utils.text import slugify


def index(request):
    error = ""
    if request.method == "POST":
        category_name = request.POST.get('category_name')

        try:
            Category.objects.create(category_name=category_name, slug=slugify(category_name))
        except Exception as e:
            print(f"Error: {e}")
            error = "yes"
    return render(request, 'index.html', {'error': error})


def add_product(request):
    error = ""
    categories = Category.objects.filter(is_deleted=False)
    if request.method == "POST":
        category = request.POST.get('category')
        product_name = request.POST.get('product_name')

        try:
            category = Category.objects.get(category_name=category)
            Product.objects.create(product_name=product_name, category=category, slug=slugify(product_name))
        except Exception as e:
            print(f"Error: {e}")
            error = "yes"
    return render(request, 'add_product.html', {'error': error, 'categories': categories})


def list_category(request):
    categories = Category.objects.filter(is_deleted=False)
    return render(request, 'list_category.html', {'categories': categories})


def list_product(request):
    products = Product.objects.filter(is_deleted=False)
    list_product = []

    for product in products:
        list_product.append({
            'product_name': product.product_name,
            'category_name': product.category.category_name,
            'id': product.id,
        })

    return render(request, 'products.html', {'list_product': list_product})


def shopped_items(request):
    return render(request, 'list.html')


def update_product(request, pid):
    product = Product.objects.get(id=pid)
    categories = Category.objects.filter(is_deleted=False)
    if request.method == "POST":
        product_name = request.POST.get('editproduct')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)
        product.product_name = product_name
        product.category = category

        product.save()

    return render(request, 'update_product.html', {'product': product, 'categories': categories})


def delete_product(request, pid):
    product = Product.objects.get(id=pid, is_deleted=False)
    product.is_deleted = True
    product.save()
    return redirect('list_product')


def delete_category(request, pid):
    category = Category.objects.get(id=pid, is_deleted=False)
    category.is_deleted = True
    category.save()
    return redirect('list_category')
