from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ImageField
from rest_framework.serializers import ModelSerializer

from apps.user.models import CourseCategory, Course, Teacher, Student, CourseNew, CourseComplain, Customer


class CourseCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


# i should do update

class CreateCourseCategoryModelSerializer(ModelSerializer):
    name = CharField()
    """
    Create Course Category
    """

    def validate(self, data):
        if CourseCategory.objects.filter(name=data['name']).exists():
            raise ValidationError('This name already taken')
        return data

    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'photo')


class ListCourseCategoryModelSerializer(ModelSerializer):
    """
    List GET all categories
    """

    class Meta:
        model = CourseCategory
        fields = '__all__'


class UpdateCourseCategoryModelSerializer(ModelSerializer):
    """

    Update CATEGORY

    """

    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'photo')


class RetrieveCourseCategoryModelSerializer(ModelSerializer):
    """
    Get obj/{id} category

    """

    class Meta:
        model = CourseCategory
        exclude = ('created_at', 'updated_at')


class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ()


class ListTeacherModelSerializer(ModelSerializer):
    direction = CourseCategoryModelSerializer(read_only=True)

    """
    List all Teachers GET
    """

    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'image', 'direction')


class TeacherListModelSerializer(ModelSerializer):
    direction = CourseCategoryModelSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'


class CreateTeacherModelSerializer(ModelSerializer):
    direction = CourseCategoryModelSerializer(read_only=True)
    """
     Create Teacher POST
    """

    class Meta:
        model = Teacher
        exclude = ('created_at', 'updated_at')


class UpdateTeacherModelSerializer(ModelSerializer):
    """

    Update Teacher obj/{id}  PUT/PATCH

    """

    class Meta:
        model = Teacher
        exclude = ('created_at', 'updated_at')


class RetrieveTeacherModelSerializer(ModelSerializer):
    direction = CourseCategoryModelSerializer(read_only=True)

    """
        GET ONE TEACHER obj/{id} RETRIEVE
    """

    class Meta:
        model = Teacher
        fields = ('id', 'image', 'rating', 'full_name', 'direction', 'description', 'url_video')


class CourseModelSerializer(ModelSerializer):
    """
       COURSE MODEL SERIALIZER
    """

    class Meta:
        model = Course
        fields = '__all__'


class ListCourseModelSerializer(ModelSerializer):
    """

    LIST ALL COURSES GET

    """

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['full_name'] = TeacherModelSerializer(instance.full_name).data
        represent['category'] = CourseCategoryModelSerializer(instance.category).data
        return represent

    class Meta:
        model = Course
        exclude = ('created_at', 'updated_at')


class CreateCourseModelSerializer(ModelSerializer):
    """
    Create COURSE POST
    """

    class Meta:
        model = Course
        exclude = ('created_at', 'updated_at')


class UpdateCourseModelSerializer(ModelSerializer):
    """
    Update Course obj/{id} PUT/PATCH
    """

    class Meta:
        model = Course
        exclude = ('created_at', 'updated_at')


class RetrieveCourseModelSerializer(ModelSerializer):
    """
    GET obj/{id} Retrieve

    """

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
        represent['teacher'] = TeacherModelSerializer(instance.teacher).data
        return represent

    class Meta:
        model = Student
        fields = ('id', 'image', 'full_name', 'course')


class StudentListModelSerializer(ModelSerializer):

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['course'] = CourseCategoryModelSerializer(instance.course).data
        represent['teacher'] = TeacherModelSerializer(instance.teacher).data
        return represent

    class Meta:
        model = Student
        fields = '__all__'


class RetrieveStudentModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['course'] = CourseCategoryModelSerializer(instance.course).data
        represent['teacher'] = TeacherModelSerializer(instance.teacher).data
        return represent

    class Meta:
        model = Student
        fields = '__all__'


class CreateStudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'full_name', 'image', 'course', 'teacher', 'description')


class UpdateStudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        exclude = ('created_at', 'updated_at')


class CourseNewModelSerializer(ModelSerializer):
    class Meta:
        model = CourseNew
        exclude = ()


class HeadCourseNewModelSerializer(ModelSerializer):
    class Meta:
        model = CourseNew
        exclude = ('created_at', 'updated_at')


class CreateCourseComplainModelSerializer(ModelSerializer):

    def validate(self, data):
        if data['phone_number'] is None:
            raise ValidationError('The phone number can not be none')

        if len(data['phone_number']) > 9:
            raise ValidationError('The phone number should be 9 numbers')

        return data

    class Meta:
        model = CourseComplain
        fields = ('id', 'first_name', 'phone_number', 'description')


class CourseComplainModelSerializer(ModelSerializer):
    class Meta:
        model = CourseComplain
        fields = '__all__'


class CustomerModelSerializer(ModelSerializer):
    course = CourseCategoryModelSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class CreateCustomerModelSerializer(ModelSerializer):

    def validate(self, data):
        if Customer.objects.filter(phone_number=data['phone_number']).exists():
            raise ValidationError('This phone_number already exists')

        if len(data['phone_number']) > 9:
            raise ValidationError('The phone number should be 9 numbers')

        return data

    class Meta:
        model = Customer
        fields = ('id', 'course', 'first_name', 'phone_number')


class UpdateCustomerModelSerializer(ModelSerializer):

    def validate(self, data):
        if len(data['phone_number']) > 9:
            raise ValidationError('The phone number should be 9 numbers')

        return data

    class Meta:
        model = Customer
        fields = ('id', 'course', 'first_name', 'phone_number', 'status')
