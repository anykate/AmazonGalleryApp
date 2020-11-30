from rest_framework import viewsets

from .models import Category, Seller
from .serializers import CategorySerializer, SellerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_url_kwarg = 'cat_id'


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    lookup_url_kwarg = 'seller_id'
