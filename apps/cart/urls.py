from django.urls import path

from apps.cart.views import CartAPIView

# 

urlpatterns = [
    path('', CartAPIView.as_view()),
]