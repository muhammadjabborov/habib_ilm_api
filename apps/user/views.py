from django.http import Http404
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.user.models import CourseCategory, Course, Teacher, Student
from apps.user.serializers import CourseCategoryModelSerializer, ListCourseCategoryModelSerializer, \
    CreateCourseCategoryModelSerializer, RetrieveCourseCategoryModelSerializer, UpdateCourseCategoryModelSerializer, \
    TeacherModelSerializer, ListTeacherModelSerializer, CreateTeacherModelSerializer, RetrieveTeacherModelSerializer, \
    UpdateTeacherModelSerializer, CourseModelSerializer, ListCourseModelSerializer, CreateCourseModelSerializer, \
    ListStudentModelSerializer, CreateStudentModelSerializer, RetrieveStudentModelSerializer, \
    UpdateStudentModelSerializer, StudentModelSerializer, UpdateCourseModelSerializer, RetrieveCourseModelSerializer


class CourseCategoryModelViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all().order_by('-created_at')
    permission_classes = [AllowAny]
    serializer_class = CourseCategoryModelSerializer
    lookup_url_kwarg = 'id'
    parser_classes = [MultiPartParser]
    search_fields = ['id', 'name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCourseCategoryModelSerializer,
            'create': CreateCourseCategoryModelSerializer,
            'retrieve': RetrieveCourseCategoryModelSerializer,
            'update': UpdateCourseCategoryModelSerializer,
        }
        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]

        return super(self.__class__, self).get_permissions()


class TeacherModelViewSet(ModelViewSet):
    queryset = Teacher.objects.all().order_by('-created_at')
    serializer_class = TeacherModelSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'last_name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListTeacherModelSerializer,
            'create': CreateTeacherModelSerializer,
            'retrieve': RetrieveTeacherModelSerializer,
            'update': UpdateTeacherModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]

        return super(self.__class__, self).get_permissions()


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('-created_at')
    serializer_class = CourseModelSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCourseModelSerializer,
            'create': CreateCourseModelSerializer,
            'update': UpdateCourseModelSerializer,
            'retrieve': RetrieveCourseModelSerializer
        }
        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(self.__class__, self).get_permissions()


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListStudentModelSerializer,
            'create': CreateStudentModelSerializer,
            'update': UpdateStudentModelSerializer,
            'retrieve': RetrieveStudentModelSerializer
        }
        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(self.__class__, self).get_permissions()
