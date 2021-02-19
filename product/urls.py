from django.urls import path
from .views import home_page, products_list, product_details

urlpatterns = [
    # name нужен для перехода страниц со страницы
    path('', home_page, name='index-page'),
    path('products/<slug:category_slug>/', products_list, name='products-list'),
    path('products/details/<int:product_id>/', product_details, name='product-details')
]




