from rest_framework import serializers

from .models import Category, Product, DiscountCode

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "left"
            )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields =(
            'discountCode',
            'discountPrcntAsDecimal',
            'discountDescription',
            'isActive',
            'discountPrcntAsNmbr'
        )