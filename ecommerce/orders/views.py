from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderdItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from django.db import transaction
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@login_required(login_url='account')
def show_cart(request) :
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
    context = {'cart': cart_obj}
    return render(request, 'cart.html',context)

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        orderd_item, created = OrderdItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if not created:
            orderd_item.quantity += quantity
        else:
            orderd_item.quantity = quantity
        orderd_item.save()

        return redirect('cart')

    
@login_required(login_url='account')  
def delete_from_cart(request, item_id):
    item = get_object_or_404(OrderdItem, pk=item_id)
    if item:
        item.delete()
    return redirect('cart')

@login_required(login_url='account')
def view_orders(request) :
    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner=customer).exclude(order_status = Order.CART_STAGE)
    context = {'orders' : all_orders}
    return render(request, 'orders.html',context)

@login_required(login_url='account')
def checkout(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, _ = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )

    total_price = 0
    for item in cart_obj.added_items.all():
        total_price += item.quantity * item.product.price

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                checkout_info = form.save(commit=False)
                checkout_info.order = cart_obj
                checkout_info.save()

                cart_obj.order_status = Order.ORDER_CONFIRMED
                cart_obj.total_price = total_price
                cart_obj.save()
                OrderdItem.objects.filter(owner=cart_obj).delete()

                email = cart_obj.owner.user.email
                subject = 'Order Placement'
                message = f'Your Order is Placed sucessfully. You need to pay ${total_price}'
                send_mail(subject,message,settings.EMAIL_HOST_USER,[email])

                messages.success(request, 'Checkout successful!')
                return redirect('cart')
    else:
        form = CheckoutForm()

    context = {
        'cart': cart_obj,
        'form': form,
        'total_price':total_price
    }
    return render(request, 'checkout.html', context)




