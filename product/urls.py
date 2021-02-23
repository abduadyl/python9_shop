from django.urls import path
from .views import ProductsListView, ProductDetailsView
from .views import HomePageView

urlpatterns = [
    # name нужен для перехода страниц со страницы
    path('', HomePageView.as_view(), name='index-page'),
    path('products/<slug:category_slug>/', ProductsListView.as_view(), name='products-list'),
    path('products/details/<int:pk>/', ProductDetailsView.as_view(), name='product-details')
]




