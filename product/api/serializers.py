from django.db.models import fields
from django.http import request
from rest_framework import serializers
from product.models import Product, Category, Size, Color, Product_image


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = [
            'id',
            'title',
        ]

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = [
            'id',
            'title',
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
    class Meta:
        model = Product_image
        fields = ('id', 'image')

 
class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.title')
    size = SizeSerializer(many=True)
    color = ColorSerializer(many=True)
    image = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'slug',
            'price',
            'discount',
            'size',
            'color',
            'short_description',
            'description',
            'category',
            'image',
            'taglar',
            'created_at',
            'set_discount_price',
            "main_image",
        ]

    def get_image(self, product):
        return ProductImageSerializer(product.product_images.all(), context=self.context, many=True).data


class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'slug',
            'price',
            'discount',
            'size',
            'color',
            'short_description',
            'description',
            'category',
            'taglar',
            'created_at',
            "main_image",
        ]



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]


