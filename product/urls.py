from django.urls import path
from .views import (ProductsListView, ProductDetailsView, HomePageView,
                    ProductDeleteView, ProductCreateView, ProductEditView)

urlpatterns = [
    path('', HomePageView.as_view(), name='index-page'),
    path('products/create/', ProductCreateView.as_view(), name='create-product'),
    path('products/<slug:category_slug>/', ProductsListView.as_view(), name='products-list'),
    path('products/details/<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
    path('products/edit/<int:pk>/', ProductEditView.as_view(), name='edit-product'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),
]




