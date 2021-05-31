from functools import partial
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product
from product.api.serializers import ProductSerializer, ProductCreateSerializer, CategorySerializer, CategoryCreateSerializer
# from rest_framework.decorators import api_view

import json

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# --------------------- Product -----------------------------------
class ProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.filter(is_published=True)
        filter_by = json.loads(json.dumps(request.GET))
        if filter_by:
            product = product.filter(**filter_by)
        serializer = ProductSerializer(product, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        product_data = request.data
        serializer = ProductCreateSerializer(data=product_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = Product.objects.filter(pk=product_id, is_published=True).first()
        if not product:
            raise NotFound
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        product_data = request.data
        product_id = kwargs.get('pk')
        product = Product.objects.filter(pk=product_id, is_published=True).first()
        if not product:
            raise NotFound
        serializer = ProductCreateSerializer(data=product_data, instance=product, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        product_data = request.data
        product_id = kwargs.get('pk')
        product = Product.objects.filter(pk=product_id, is_published=True).first()
        if not product:
            raise NotFound
        serializer = ProductCreateSerializer(data=product_data, instance=product,
                                            partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = Product.objects.filter(pk=product_id, is_published=True)
        if not product:
            raise NotFound
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(('GET', 'POST'))
# def product(request):
#     if request.method == 'POST':
#         product_data = request.data
#         serializer = ProductCreateSerializer(data=product_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     products = Product.objects.filter(is_published=True)
#     serializer = ProductSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, slug):
#     try:
#         product = Product.objects.get(slug=slug)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductCreateSerializer(product, data=request.data, partial= True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# ----------------------Category-------------------



class CategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        filter_by = json.loads(json.dumps(request.GET))
        if filter_by:
            categories = categories.filter(**filter_by)
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        category_data = request.data
        serializer = CategoryCreateSerializer(data=category_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        category = Category.objects.filter(pk=category_id).first()
        if not category:
            raise NotFound
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        category_data = request.data
        category_id = kwargs.get('pk')
        category = Category.objects.filter(pk=category_id).first()
        if not category:
            raise NotFound
        serializer = CategoryCreateSerializer(data=category_data, instance=category, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        category_data = request.data
        category_id = kwargs.get('pk')
        category = Category.objects.filter(pk=category_id).first()
        if not category:
            raise NotFound
        serializer = CategoryCreateSerializer(data=category_data, instance=category,
                                            partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        category = Category.objects.filter(pk=category_id)
        if not category:
            raise NotFound
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(('GET', 'POST'))
# def category(request):
#     if request.method == 'POST':
#         category_data = request.data
#         serializer = CategoryCreateSerializer(data=category_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     categories = Category.objects.all()
#     serializer = CategorySerializer(categories, many=True, context={'request': request})
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CategorySerializer(category, data=request.data, partial= True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)