from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .serializers import ProductSerializer, CategorySerializer
from ..models import Product, Category


class CategoryAPIView(generics.ListCreateAPIView):
    ueryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductAPIView(APIView):
    serializer_class = ProductSerializer
    model = Product

    def get_instance(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is not None:
            product = self.get_instance(pk)
            serializer = self.serializer_class(product)
            return Response(serializer.data)
        else:
            products = self.model.objects.all()
            serializer = self.serializer_class(products, many=True)
            return Response(serializer.data)

    def post(self, request, pk=None, format=None):
        if pk is not None:
            product = self.get_instance(pk)
            serializer = self.serializer_class(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_instance(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
