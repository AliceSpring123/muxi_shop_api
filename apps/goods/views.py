from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.goods.models import Goods
from apps.goods.serializer import GoodsSerializer
from utils.ResponseMsg import GoodsResponse


# Create your views here.
# http://127.0.0.1:8000/goods/category/1
class GoodsCategoryAPIView(APIView):
    def get(self, request, category_id, page):

        print("get 请求莱拉")

        # 配置显示多少条数据
        current_page = (page-1) * 20
        end_data = page * 20
        category_data = Goods.objects.filter(
            type_id = category_id
        ).all()[current_page:end_data]

        result = GoodsSerializer(instance=category_data, many=True)
        return GoodsResponse.success(result.data)

    