from django.db import transaction
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cart.models import ShoppingCart
from apps.cart.serializers import ShoppingCartSerializer
from utils.ResponseMsg import CartResponse


# Create your views here.

# 购物车添加新商品 & 已加商品复选
# http://127.0.0.1:8000/cart/
class ShoppingCartAPIView(APIView):
    # 购物车应登录后方可访问
    # @todo 后续补充登录权限验证

    # 获取购物车数据
    # http://127.0.0.1:8000/cart?email=123444@qq.com
    def get(self, request):
        # 找到此账户下的购物车数据
        email = request.GET.get('email')

        print(email)
        cart_data = ShoppingCart.objects.filter(email=email).all()
        print(cart_data)
        # 反序列化数据回传前端
        result = ShoppingCartSerializer(instance=cart_data, many=True)
        print(type(result))

        return CartResponse.success(result.data, "数据请求成功")

    # 添加购物车
    # http://127.0.0.1:8000/cart/
    # body: JSON
    # {
    #     "email": "123444@q1q.com",
    #     "sku_id": "334",
    #     "nums": 1,
    #     "is_delete": 0
    # }
    def post(self, request):
        # 验证请求数据
        serializer = ShoppingCartSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': '数据验证失败',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        # 获取验证后的数据
        request_data= serializer.validated_data
        email = request_data['email']
        sku_id = request_data['sku_id']
        nums = request_data['nums']

        # 商品存在 -> 更新数量
        try:
            # 使用原子事务确保数据一致性
            with transaction.atomic():
                # 尝试获取已存在的记录
                existed_data = ShoppingCart.objects.get(
                    email=email,
                    sku_id=sku_id,
                    is_delete=0
                )

                # 存在 -> 更新数量并保存
                print("商品已在购物车，更新记录")
                existed_data.nums += nums
                existed_data.save()  # 保存数据！

                # 向前端返回更新后的数据
                result = ShoppingCartSerializer(instance=existed_data)
                return CartResponse.success(result.data, msg="更新记录")

        # 不存在 -> 创建新记录
        except ShoppingCart.DoesNotExist:
            print("商品不在购物车，新建记录")
            new_cart_item = ShoppingCart.objects.create(
                email=email,
                sku_id=sku_id,
                nums=nums,  # 使用请求中的数量
                is_delete=0
            )
            # 向前端返回新建的数据
            result = ShoppingCartSerializer(instance=new_cart_item)
            return CartResponse.success(result.data, "创建新记录")

        # 有多条重复记录 -> 处理重复记录异常
        except ShoppingCart.MultipleObjectsReturned:
            print("错误：找到多条重复记录！进行数据清理")
            # 获取第一条记录，删除其他重复记录
            first_item = ShoppingCart.objects.filter(
                email=email,
                sku_id=sku_id,
                is_delete=0
            ).first()
            # 删除其他重复记录
            ShoppingCart.objects.filter(
                email=email,
                sku_id=sku_id,
                is_delete=0
            ).exclude(id=first_item.id).update(is_delete=1)
            # 更新第一条记录的数量
            first_item.nums += nums
            first_item.save()
            # 向前端返回数据
            result = ShoppingCartSerializer(instance=first_item)
            CartResponse.success(result.data, msg="警告：多条重复记录！")

        except Exception as e:
            # 7. 记录日志并返回错误信息
            print(f"添加购物车失败: {str(e)}")
            # 实际项目中应该使用日志系统，如 logger.error(...)
            return CartResponse.failed(result.data)




