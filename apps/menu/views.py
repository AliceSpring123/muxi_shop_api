import json

from django.http import HttpResponse
from django.views import View

from apps.menu.models import MainMenu, SubMenu
from apps.menu.serializers import MainMenuSerializer, SubMenuSerializer
from utils import ResponseMsg


# Create your views here.
# main_menu api
# example:
# http://localhost:8000/menu/main_menu/
class GoodsMainMenu(View):
    def get(self,request):
        print("get请求来啦")
        main_menu = MainMenu.objects.all()
        result=MainMenuSerializer(instance=main_menu,many=True)
        return ResponseMsg.MenuResponse.success(result.data)

    def post(self,request):
        print("post请求来啦")
        return HttpResponse("post请求")

# sub_menu api
# example:
# http://localhost:8000/menu/sub_menu?main_menu_id=1
class GoodsSubMenu(View):
    def get(self,request):
        # 获取请求的参数
        param_id = request.GET["main_menu_id"]
        print(param_id)
        # 拿到二级菜单的内容
        sub_menu = SubMenu.objects.filter(main_menu_id=param_id).all()
        result = SubMenuSerializer(instance=sub_menu,many=True)
        return ResponseMsg.MenuResponse.success(result.data)