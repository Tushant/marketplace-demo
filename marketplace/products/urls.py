from django.urls import path

from .views import ProductView, ProductForm, home, products_with_category
from .api.views import ProductAPIView

app_name = 'products'

urlpatterns = [
    path('', home, name="home"),
    path('products', ProductView.as_view(), name="products-list"),
    path('products/category/<int:category_id>',
         products_with_category, name="products-with-category"),
    path('product/<int:pk>', ProductView.as_view(), name="product-detail"),
    path('product/add', ProductForm.as_view(), name="product-add"),
    path('product/<int:pk>/edit', ProductForm.as_view(), name="product-update"),

    # for rest api
    path('products-list', ProductAPIView.as_view(), name="products-list-api"),
    path('product-add', ProductAPIView.as_view(), name="products-add-api"),
    path('product-detail/<int:pk>', ProductAPIView.as_view(),
         name="product-detail-api"),
    path('product-edit/<int:pk>',
         ProductAPIView.as_view(), name="products-edit-api"),
]
