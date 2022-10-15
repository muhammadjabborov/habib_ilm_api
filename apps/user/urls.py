from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.views import CourseCategoryModelViewSet, TeacherModelViewSet, CourseAPIView

router = DefaultRouter()
router.register('course-category', CourseCategoryModelViewSet)
router.register('teacher', TeacherModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('course/', CourseAPIView.as_view(), name='course')
]
