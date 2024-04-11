from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from products import views 

urlpatterns = [
    path('',views.index,name='home'),
    path('products',views.product_list,name='products'),
    path('products_details/<pk>',views.detail_product,name='products_details'),
    path('review/<int:pk>',views.review,name='review'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)