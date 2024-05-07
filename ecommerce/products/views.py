from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q
from customers.models import Customer
from django.contrib.auth.decorators import login_required
from .models import Review

# Create your views here.

def index(request) :
    featured_product = Product.objects.order_by('priority')[:4]
    latest_product = Product.objects.order_by('-id')[:4]
    context = {
        'featured_product':featured_product,
        'latest_product':latest_product
    }
    return render(request,'index.html',context)

def product_list(request):
    page = 1
    search_query = request.GET.get('q', '')
    
    if request.GET:
        page = request.GET.get('page', 1)
        sort_by = request.GET.get('sort_by', 'priority')

        if sort_by == 'price':
            list_product = Product.objects.order_by('-price')
        elif sort_by == 'name':
            list_product = Product.objects.order_by('title')
        else:
            list_product = Product.objects.order_by('priority')

        if search_query:
            list_product = list_product.filter(Q(title__icontains=search_query))
    else:
        list_product = Product.objects.order_by('priority')

    product_paginator = Paginator(list_product, 2)
    list_product = product_paginator.get_page(page)

    context = {
        'list_products': list_product,
        'sort_by': request.GET.get('sort_by', 'priority')
    }
    return render(request, 'products.html', context)


def detail_product(request,pk) :
    product = Product.objects.get(pk=pk)
    context = {'product':product}
    return render(request, 'product_detail.html', context)

@login_required(login_url='account')
def review(request,pk):
    products = get_object_or_404(Product,pk=pk)
    user_detail = request.user.customer_profile
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        review = request.POST.get('item_review')
 
        item_reviews = Review.objects.create(user = user_detail,product = products,rating=star_rating,review_desp=review)
        item_reviews.save()
 
    rating_details = Review.objects.filter(product=products)
 
    return render(request,'review.html',{'rating_details':rating_details})