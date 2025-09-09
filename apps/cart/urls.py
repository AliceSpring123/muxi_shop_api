from django.urls import path

from apps.cart.views import ShoppingCartAPIView

# 

urlpatterns = [
    path('', ShoppingCartAPIView.as_view()),
]