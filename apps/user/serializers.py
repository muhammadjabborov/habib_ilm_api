from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ImageField
from rest_framework.serializers import ModelSerializer

from apps.user.models import CourseCategory


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