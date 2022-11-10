from django.contrib.auth.models import User
from django.db.models import Count
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.admins.serializers import UserDataSerializer
from apps.shared.pagination import CourseCategoryPagination, TeacherPagination, CoursePagination, StudentPagination, \
    CourseNewPagination, ComplainPagination, CustomerPagination, CustomerTodayPagination
from apps.user.filters import CustomerFilter
from apps.user.models import CourseCategory, Course, Teacher, Student, CourseNew, CourseComplain, Customer
from apps.user.serializers import CourseCategoryModelSerializer, ListCourseCategoryModelSerializer, \
    TeacherModelSerializer, ListTeacherModelSerializer, CreateTeacherModelSerializer, RetrieveTeacherModelSerializer, \
    UpdateTeacherModelSerializer, CourseModelSerializer, ListCourseModelSerializer, CreateCourseModelSerializer, \
    ListStudentModelSerializer, CreateStudentModelSerializer, RetrieveStudentModelSerializer, \
    UpdateStudentModelSerializer, StudentModelSerializer, UpdateCourseModelSerializer, RetrieveCourseModelSerializer, \
    CourseNewModelSerializer, HeadCourseNewModelSerializer, CourseComplainModelSerializer, \
    CreateCourseComplainModelSerializer, CustomerModelSerializer, CreateCustomerModelSerializer, \
    UpdateCustomerModelSerializer, StudentListModelSerializer, TeacherListModelSerializer
from apps.user.serializers import CreateCourseCategoryModelSerializer, RetrieveCourseCategoryModelSerializer, \
    UpdateCourseCategoryModelSerializer


class CourseCategoryModelViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all().order_by('-created_at')
    permission_classes = [AllowAny]
    serializer_class = CourseCategoryModelSerializer
    lookup_field = 'slug'
    pagination_class = CourseCategoryPagination
    parser_classes = (MultiPartParser, FormParser,)
    search_fields = ['id', 'name']
    filter_backends = [SearchFilter]

    #    def create(self, request, *args, **kwargs):
    #     """
    #         FOR CREATE
    #     """
    #     return super().create(request, *args, **kwargs)

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
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()


class GetCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teacher_count = Teacher.objects.count()
        student_count = Student.objects.count()
        customer_count = Customer.objects.filter(status="Kutilyapti").count()

        data = {
            'Ustozlar': teacher_count,
            'Oquvchilar': student_count,
            'Bugungi_Arizalar': customer_count
        }
        return Response(data)


class TeacherModelViewSet(ModelViewSet):
    queryset = Teacher.objects.order_by('-created_at')
    serializer_class = TeacherModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = TeacherPagination
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

        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-teacher',
            serializer_class=TeacherListModelSerializer, pagination_class=TeacherPagination)
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherListModelSerializer(teachers, many=True)
        return Response(serializer.data)


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('-created_at')
    serializer_class = CourseModelSerializer
    permission_classes = [AllowAny]
    pagination_class = CoursePagination
    filter_backends = [SearchFilter]
    lookup_url_kwarg = 'id'
    parser_classes = (MultiPartParser, FormParser,)

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
        return super().get_permissions()


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = StudentPagination
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
        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-student',
            serializer_class=StudentListModelSerializer, pagination_class=StudentPagination)
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentListModelSerializer(students, many=True)
        return Response(serializer.data)


class CourseNewModelViewSet(ModelViewSet):
    queryset = CourseNew.objects.all().order_by('-created_at')
    serializer_class = CourseNewModelSerializer
    pagination_class = CourseNewPagination
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
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

        return super().get_permissions()


class CourseComplainModelViewSet(ModelViewSet):
    queryset = CourseComplain.objects.all().order_by('-created_at')
    serializer_class = CourseComplainModelSerializer
    pagination_class = ComplainPagination
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

        return super().get_permissions()



class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerModelSerializer
    pagination_class = CustomerPagination
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'phone_number', 'first_name']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CustomerFilter

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
        return super().get_permissions()

    @action(detail=False, methods=['GET'], url_path='today-orders', serializer_class=serializer_class,
            pagination_class=CustomerTodayPagination)
    def today_customers(self, request):
        """
        GET today orders
        """
        customers = Customer.objects.filter(status='Kutilyapti').order_by('-created_at')
        serializer = self.serializer_class(customers, many=True)
        return Response(serializer.data)
