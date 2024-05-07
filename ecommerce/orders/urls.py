from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from orders import views 

urlpatterns = [
    path('cart',views.show_cart,name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('cart/delete/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('view_orders',views.view_orders,name='view_orders'),
    path('checkout',views.checkout,name='checkout'),
]
