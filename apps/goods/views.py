from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.goods.models import Goods
from apps.goods.serializer import CategorySerializer, GoodsDetailSerializer
from utils.ResponseMsg import GoodsResponse


# Create your views here.
# 获取某一类下的所有商品
# http://127.0.0.1:8000/goods/category/<int:category_id>/<int:page>/
class GoodsCategoryAPIView(APIView):
    def get(self, request, category_id, page):
        # 每页显示20条数据
        current_page = (page - 1) * 20
        end_data = page * 20
        category_data = Goods.objects.filter(
            type_id = category_id
        ).all()[current_page:end_data]

        result = CategorySerializer(instance=category_data, many=True)
        return GoodsResponse.success(result.data)

# 获取某个商品详情
# http://127.0.0.1:8000/goods/detail/<sku_id>/
class GoodsDetailAPIView(APIView):
    def get(self, request, sku_id):
        goods_data=Goods.objects.filter(
            sku_id = sku_id
        ).filter()

        result = GoodsDetailSerializer(instance=goods_data, many=True)
        return GoodsResponse.success(result.data)