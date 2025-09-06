import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.menu.models import MainMenu, SubMenu
from apps.menu.serializers import MainMenuSerializer
from utils import ResponseMsg


# Create your views here.
class GoodsMainMenu(View):
    def get(self,request):
        print("get请求来啦")
        main_menu = MainMenu.objects.all()
        result = MainMenuSerializer(instance=main_menu)
        return ResponseMsg.MenuResponse.success(result.data)

    def post(self,request):
        print("post请求来啦")
        return HttpResponse("post请求")

class GoodsSubMenu(View):
    def get(self,request):
        # 获取请求的参数
        param_id = request.GET["main_menu_id"]
        # 拿到二级菜单的内容
        sub_menu = SubMenu.objects.filter(main_menu_id=param_id)
        result = MainMenuSerializer(instance=param_id)
        return ResponseMsg.MenuResponse.success(result.data)