from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.shared.pagination import CourseDetailsPagination
from apps.user.models import CourseDetails, Course, Teacher, Student, CourseNew, CourseComplain, Customer
from apps.user.serializers import CourseDetailsModelSerializer, ListCourseDetailsModelSerializer, \
    TeacherModelSerializer, ListTeacherModelSerializer, CreateTeacherModelSerializer, RetrieveTeacherModelSerializer, \
    UpdateTeacherModelSerializer, CourseModelSerializer, ListCourseModelSerializer, CreateCourseModelSerializer, \
    ListStudentModelSerializer, CreateStudentModelSerializer, RetrieveStudentModelSerializer, \
    UpdateStudentModelSerializer, StudentModelSerializer, UpdateCourseModelSerializer, RetrieveCourseModelSerializer, \
    CourseNewModelSerializer, HeadCourseNewModelSerializer, CourseComplainModelSerializer, \
    CreateCourseComplainModelSerializer, CustomerModelSerializer, CreateCustomerModelSerializer, \
    UpdateCustomerModelSerializer
from apps.user.serializers import CreateCourseDetailsModelSerializer, RetrieveCourseDetailsModelSerializer, \
    UpdateCourseDetailsModelSerializer


class CourseDetailsModelViewSet(ModelViewSet):
    queryset = CourseDetails.objects.all().order_by('-created_at')
    permission_classes = [AllowAny]
    serializer_class = CourseDetailsModelSerializer
    lookup_url_kwarg = 'id'
    pagination_class = CourseDetailsPagination
    parser_classes = [MultiPartParser]
    search_fields = ['id', 'name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCourseDetailsModelSerializer,
            'create': CreateCourseDetailsModelSerializer,
            'retrieve': RetrieveCourseDetailsModelSerializer,
            'update': UpdateCourseDetailsModelSerializer,
        }
        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsAuthenticated]
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
            'create': TeacherModelSerializer,
            'retrieve': RetrieveTeacherModelSerializer,
            'update': UpdateTeacherModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super(self.__class__, self).get_permissions()


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('-created_at')
    serializer_class = CourseModelSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
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
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super(self.__class__, self).get_permissions()


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'title', 'description']
    filter_backends = [SearchFilter]

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
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super(self.__class__, self).get_permissions()


class CourseNewModelViewSet(ModelViewSet):
    queryset = CourseNew.objects.all().order_by('-created_at')
    serializer_class = CourseNewModelSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'title', 'description']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'create': HeadCourseNewModelSerializer,
            'update': HeadCourseNewModelSerializer
        }
        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['update', 'create', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]

        else:
            self.permission_classes = [AllowAny]

        return super(self.__class__, self).get_permissions()


class CourseComplainModelViewSet(ModelViewSet):
    queryset = CourseComplain.objects.all().order_by('-created_at')
    serializer_class = CourseComplainModelSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'phone_number']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'create': CreateCourseComplainModelSerializer,
            'update': CreateCourseComplainModelSerializer
        }
        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['update', 'create', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]

        else:
            self.permission_classes = [AllowAny]

        return super(self.__class__, self).get_permissions()


class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerModelSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'phone_number', 'first_name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'create': CreateCustomerModelSerializer,
            'update': UpdateCustomerModelSerializer
        }
        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(self.__class__, self).get_permissions()
