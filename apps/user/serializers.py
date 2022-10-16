from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ImageField
from rest_framework.serializers import ModelSerializer

from apps.user.models import CourseCategory, Course, Teacher, Student


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
        fields = ('id', 'full_name', 'image', 'direction')


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
        fields = ('id', 'image', 'rating', 'full_name', 'direction', 'description', 'url_video')


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ListCourseModelSerializer(ModelSerializer):

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['full_name'] = TeacherModelSerializer(instance.full_name).data
        represent['category'] = CourseCategoryModelSerializer(instance.category).data
        return represent

    class Meta:
        model = Course
        exclude = ('created_at', 'updated_at')


class CreateCourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ('created_at', 'updated_at')


class UpdateCourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ('created_at', 'updated_at')


class RetrieveCourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ListStudentModelSerializer(ModelSerializer):

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['course'] = CourseCategoryModelSerializer(instance.course).data
        return represent

    class Meta:
        model = Student
        fields = ('id', 'image', 'full_name', 'course')


class RetrieveStudentModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['course'] = CourseCategoryModelSerializer(instance.course).data
        return represent

    class Meta:
        model = Student
        fields = '__all__'


class CreateStudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'image', 'course', 'description')


class UpdateStudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        exclude = ('created_at', 'updated_at')
