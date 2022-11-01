from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
