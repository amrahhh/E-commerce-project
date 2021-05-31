from rest_framework import serializers
from checkout.models import OrderItem
from django.contrib.auth import  get_user_model
from product.api.serializers import ProductSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
            'bio',
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'quantity',
            'author',
            'get_total_price',
        ]


class OrderItemCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'quantity',
            'author',
        ]

    def validate(self, data):
        request = self.context.get('request')
        data['author'] = request.user
        attrs = super().validate(data)
        return attrs