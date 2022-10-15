from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.user.models import CourseCategory, Course, Teacher
from apps.user.serializers import CourseCategoryModelSerializer, ListCourseCategoryModelSerializer, \
    CreateCourseCategoryModelSerializer, RetrieveCourseCategoryModelSerializer, UpdateCourseCategoryModelSerializer, \
    TeacherModelSerializer, ListTeacherModelSerializer, CreateTeacherModelSerializer, RetrieveTeacherModelSerializer, \
    UpdateTeacherModelSerializer, CourseModelSerializer, ListCourseModelSerializer, CreateCourseModelSerializer


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
            'create': CreateTeacherModelSerializer,
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


class CourseAPIView(GenericAPIView):
    queryset = Course.objects.all().order_by('created_at')
    serializer_class = CourseModelSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    parser_classes = [MultiPartParser]

    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = ListCourseModelSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateCourseModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
