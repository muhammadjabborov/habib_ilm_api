from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.views import CourseCategoryModelViewSet

router = DefaultRouter()
router.register('course-category', CourseCategoryModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]