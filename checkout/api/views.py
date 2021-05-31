from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from checkout.api.serializers import OrderItemSerializer, OrderItemCreateSerializer
from checkout.models import OrderItem

from product.models import Product


class OrderItemAPIView(APIView):

    def get(self, request, *args, **kwargs):
        order_item = OrderItem.objects.filter(author=request.user)
        serializer = OrderItemSerializer(order_item, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        order_data = request.data
        product_id = order_data['product']
        product = Product.objects.filter(id=product_id).first()
        basket = OrderItem.objects.filter(product=product, author=request.user).first()
        serializer = OrderItemCreateSerializer(data=order_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if basket and order_data['quantity'] == 1 :
            basket.quantity  += 1
            basket.save()
        elif basket and order_data['quantity'] == 2:
            basket.quantity -= 1
            basket.save()
        else:
            serializer.save(product=product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    
class OrderItemDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = Product.objects.filter(pk=product_id, is_published=True).first()
        if not product:
            raise NotFound
        serializer = OrderItemSerializer(product, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        product_data = request.data
        product_id = kwargs.get('pk')
        product = Product.objects.filter(pk=product_id, is_published=True).first()
        if not product:
            raise NotFound
        serializer = OrderItemCreateSerializer(data=product_data, instance=product, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = OrderItem.objects.filter(pk=product_id)
        if not product:
            raise NotFound
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
