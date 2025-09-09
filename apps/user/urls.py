from django.urls import path

from apps.user.views import UserAPIView

urlpatterns = [
    path('', UserAPIView.as_view())
]