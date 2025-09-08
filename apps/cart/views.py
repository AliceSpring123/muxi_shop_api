from django.http import HttpResponse
from rest_framework.views import APIView


# Create your views here.

# 购物车添加新商品 & 已加商品复选
# http://127.0.0.1:8000/cart/
class CartAPIView(APIView):
    # 购物车应登录后方可访问
    # @todo 后续补充登录权限验证

    def post(self, request):
        request_data= request.data
        print(request_data)
        print(type(request_data))
        return HttpResponse("OK")