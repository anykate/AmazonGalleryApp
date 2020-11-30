from django.urls import path, include
from . import views, viewsets
# from rest_framework import routers

category_list = viewsets.CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

category_detail = viewsets.CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

seller_list = viewsets.SellerViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

seller_detail = viewsets.SellerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

# router = routers.DefaultRouter()
# router.register('sellers', viewsets.SellerViewSet)


app_name = 'products'

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.EndpointList.as_view(), name='index'),
    path('sellers/', seller_list, name='seller-list'),
    path('sellers/<int:seller_id>/', seller_detail, name='seller-detail'),
    path('categories/', category_list, name='category-list'),
    path('categories/<int:cat_id>/', category_detail, name='category-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products-filter/', views.ProductListAPIView.as_view(),
         name='products-filter'),
]
