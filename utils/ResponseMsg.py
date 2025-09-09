from django.http import HttpResponse, JsonResponse
import json

class MenuResponse():

    @staticmethod
    def success(data):
        result = {"status":1000,"data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 1001, "data": data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def other(data):
        result = {"status": 1002, "data": data}
        return JsonResponse(result,safe=False)


# 商品的响应都以 2 开头
class GoodsResponse():

    @staticmethod
    def success(data):
        result = {"status":2000,"data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 2001, "data": data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def other(data):
        result = {"status": 2002, "data": data}
        return JsonResponse(result,safe=False)
    

# 购物车相应都以 3 开头
class CartResponse():

    @staticmethod
    def success(data, msg):
        result = {"status":3000,"success": True, "message": msg, "data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 3001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 3002, "data": data}
        return JsonResponse(result, safe=False)

# 用户响应都以 4 开头
class UserResponse():

    @staticmethod
    def success(data, msg):
        result = {"status":4000,"success": True, "message": msg, "data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data, msg):
        result = {"status": 4000, "success": True, "message": msg, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def others(data, msg):
        result = {"status": 4000, "success": True, "message": msg, "data": data}
        return JsonResponse(result, safe=False)