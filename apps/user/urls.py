from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from root import settings
from apps.user.views import CourseCategoryModelViewSet, TeacherModelViewSet, \
    StudentModelViewSet, CourseModelViewSet, CourseNewModelViewSet, CourseComplainModelViewSet

router = DefaultRouter()
router.register('course-category', CourseCategoryModelViewSet)
router.register('teacher', TeacherModelViewSet)
router.register('student', StudentModelViewSet)
router.register('course', CourseModelViewSet)
router.register('course-new', CourseNewModelViewSet)
router.register('course-complain', CourseComplainModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
