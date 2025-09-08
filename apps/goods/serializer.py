from rest_framework import serializers

from apps.goods.models import Goods


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class GoodsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'