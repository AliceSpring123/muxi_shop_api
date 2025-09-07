from django.urls import path

from apps.menu.views import GoodsSubMenu, GoodsMainMenu

urlpatterns = [
    path('main_menu/', GoodsMainMenu.as_view(), name='main_menu'),
    path('sub_menu/', GoodsSubMenu.as_view(), name='submenu'),
]