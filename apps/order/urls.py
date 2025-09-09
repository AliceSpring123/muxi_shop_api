from django.urls import path

from apps.order.views import OrderGoodsGenericAPIView

urlpatterns = [
    path('goods/', OrderGoodsGenericAPIView.as_view()),
]

