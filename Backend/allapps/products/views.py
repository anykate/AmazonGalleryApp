from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer, ProductsAllInfoSerializer


# Create your views here.
class ProductList(APIView):
    '''
    List all products or create a new one
    '''

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EndpointList(APIView):
    '''
    List all possible endpoints
    '''

    def get(self, request):
        return Response({
            'sellers': 'http://localhost:8000/sellers/',
            'categories': 'http://localhost:8000/categories/',
            'products': 'http://localhost:8000/products/',
        })


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_fields = ['category__id']
    search_fields = ['title']
