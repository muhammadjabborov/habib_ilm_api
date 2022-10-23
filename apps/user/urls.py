from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from root import settings
from apps.user.views import CourseDetailsModelViewSet, TeacherModelViewSet, \
    StudentModelViewSet, CourseModelViewSet, CourseNewModelViewSet, CourseComplainModelViewSet, CustomerModelViewSet

router = DefaultRouter()
router.register('course-details', CourseDetailsModelViewSet)
router.register('teacher', TeacherModelViewSet)
router.register('student', StudentModelViewSet)
router.register('course', CourseModelViewSet)
router.register('course-new', CourseNewModelViewSet)
router.register('course-complain', CourseComplainModelViewSet)
router.register('customer',CustomerModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
