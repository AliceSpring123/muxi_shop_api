from django.urls import path

from apps.goods import views

urlpatterns = [
    path('category/<int:category_id>/<page>/', views.GoodsCategoryAPIView.as_view(), name='goods_category'),
]