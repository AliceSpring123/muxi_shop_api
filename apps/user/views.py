import copy

from django.db import transaction
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.serializer import UserSerializer
from utils import ResponseMsg

# Create your views here.
class UserAPIView(APIView):

    # 用户注册
    # http://127.0.0.1:8000/user/
    def post(self, request):
        # 复制数据以避免修改原始请求数据
        request_data = request.data.copy()
        # 验证请求数据
        serializer  = UserSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        # 创建用户（使用事务保证原子性）
        with transaction.atomic():
            user = serializer.save()

        # 返回前端
        result = UserSerializer(instance=user)
        return ResponseMsg.UserResponse.success(result.data, "注册成功")

    # 获取个人信息
    # http://127.0.0.1:8000/user?email=<email>
    def get(self, request):
        email = request.GET.get("email")
        try:
            user_info = User.objects.get(email=email)
            result = UserSerializer(instance=user_info)
            return ResponseMsg.UserResponse.success(result.data, "个人信息查询成功")
        except User.DoesNotExist as e:
            return ResponseMsg.UserResponse.success(str(e), "个人信息查询失败")