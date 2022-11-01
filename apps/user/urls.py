from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from root import settings
from apps.user.views import CourseCategoryModelViewSet, TeacherModelViewSet, \
    StudentModelViewSet, CourseModelViewSet, CourseNewModelViewSet, CourseComplainModelViewSet, CustomerModelViewSet, \
    GetCountAPIView

router = DefaultRouter()
router.register('course-cateogry', CourseCategoryModelViewSet)
router.register('teacher', TeacherModelViewSet)
router.register('student', StudentModelViewSet)
router.register('course', CourseModelViewSet)
router.register('course-new', CourseNewModelViewSet)
router.register('course-complain', CourseComplainModelViewSet)
router.register('customer', CustomerModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-count/', GetCountAPIView.as_view())
]
