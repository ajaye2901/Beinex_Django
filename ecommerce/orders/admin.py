from django.contrib import admin
from orders.models import Order, OrderdItem, CheckoutInfo
# Register your models here.

class OrderAdmin(admin.ModelAdmin) :
    list_filter = [
        "owner",
        "order_status",
        "created_at"
    ]
    search_fields = (
        "owner",
        "id",
    )
    list_display = ['id', 'owner', 'order_status', 'total_price', 'total_quantity',]

    def total_quantity(self, obj):
        return sum(item.quantity for item in obj.added_items.all())

    total_quantity.short_description = 'Total Quantity'


admin.site.register(Order, OrderAdmin)

class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'quantity', 'owner']

    list_filter = [
        "owner",
        "product__id",
    ]

    search_fields = ("owner", "product__id")

    def product_id(self, obj):
        return obj.product_id

    product_id.short_description = 'Product ID'

admin.site.register(OrderdItem, OrderedItemAdmin)

class Checkout(admin.ModelAdmin) :
    list_display = ['full_name', 'address', 'mobile_no']
    
admin.site.register(CheckoutInfo,Checkout)