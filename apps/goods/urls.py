from django.urls import path

from apps.goods.views import GoodsCategoryAPIView,GoodsDetailAPIView

urlpatterns = [
    path('category/<int:category_id>/<int:page>/', GoodsCategoryAPIView.as_view(), name='goods_category'),
    path('detail/<str:sku_id>/', GoodsDetailAPIView.as_view(), name='goods_category'),
]