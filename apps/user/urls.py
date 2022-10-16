from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.views import CourseCategoryModelViewSet, TeacherModelViewSet, \
    StudentModelViewSet, CourseModelViewSet

router = DefaultRouter()
router.register('course-category', CourseCategoryModelViewSet)
router.register('teacher', TeacherModelViewSet)
router.register('student', StudentModelViewSet)
router.register('course', CourseModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
