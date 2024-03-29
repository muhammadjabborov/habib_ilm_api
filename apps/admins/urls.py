from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.admins.views import RegisterAPIView
from apps.admins.views import UserDataAPIView

urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterAPIView.as_view(), name='register'),
    path('user/info/', UserDataAPIView.as_view(), name='info')
]
