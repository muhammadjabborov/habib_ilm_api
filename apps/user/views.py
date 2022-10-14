from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.user.models import CourseCategory
from apps.user.serializers import CourseCategoryModelSerializer, ListCourseCategoryModelSerializer, \
    CreateCourseCategoryModelSerializer, RetrieveCourseCategoryModelSerializer, UpdateCourseCategoryModelSerializer


class CourseCategoryModelViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all().order_by('-created_at')
    permission_classes = [AllowAny, ]
    serializer_class = CourseCategoryModelSerializer
    lookup_url_kwarg = 'id'
    parser_classes = [MultiPartParser, ]
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
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [AllowAny, ]

        return super(self.__class__, self).get_permissions()

# 12323