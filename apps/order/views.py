from django.http import JsonResponse
from rest_framework.generics import GenericAPIView

from apps.order.models import OrderGoods
from apps.order.serializer import OrderGoodsSerializer


# Create your views here.
class OrderGoodsGenericAPIView(GenericAPIView):
    queryset = OrderGoods.objects
    serializer_class = OrderGoodsSerializer

    def post(self, request):
        # 数据验证
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 数据写入
        serializer.save()
        return JsonResponse("ok", safe=False)


