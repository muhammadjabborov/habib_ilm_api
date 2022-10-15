from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ImageField
from rest_framework.serializers import ModelSerializer

from apps.user.models import CourseCategory, Course, Teacher


class CourseCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class CreateCourseCategoryModelSerializer(ModelSerializer):
    name = CharField()

    def validate(self, data):
        if CourseCategory.objects.filter(name=data['name']).exists():
            raise ValidationError('This name already taken')
        return data

    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'photo')


class ListCourseCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class UpdateCourseCategoryModelSerializer(ModelSerializer):
    name = CharField(required=False)
    photo = ImageField(required=False)

    def validate(self, data):
        if CourseCategory.objects.filter(name=data['name']).exists():
            raise ValidationError('This category name already exists')
        return data

    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'photo')


class RetrieveCourseCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        exclude = ('created_at', 'updated_at')


class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ()


class ListTeacherModelSerializer(ModelSerializer):
    direction = CourseCategoryModelSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'image', 'direction')


class CreateTeacherModelSerializer(ModelSerializer):
    direction = CourseCategoryModelSerializer(read_only=True)

    class Meta:
        model = Teacher
        exclude = ('created_at', 'updated_at')


class UpdateTeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('created_at', 'updated_at')


class RetrieveTeacherModelSerializer(ModelSerializer):
    direction = CourseCategoryModelSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ('id', 'image', 'rating', 'first_name', 'last_name', 'direction', 'description', 'url_video')

# class ListCourseModelSerializer(ModelSerializer):
#
#     def to_representation(self, instance):
#         represent = super().to_representation(instance)
#         represent['']
#         represent['category'] = CourseCategoryModelSerializer(instance.category).data
#         return represent
