from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CharField, SlugField, ImageField, ForeignKey, CASCADE, PROTECT, FloatField, IntegerField
from django.utils.text import slugify

from apps.shared.models import BaseModel


class CourseCategory(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField()
    photo = ImageField(upload_to='icons/')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Teacher(BaseModel):
    full_name = CharField(max_length=255)
    direction = ForeignKey(CourseCategory, on_delete=PROTECT)
    image = ImageField(upload_to='icons/')
    rating = FloatField(
        validators=[
            MaxValueValidator(5, 'Should be 5'),
            MinValueValidator(1, 'Should be 1')
        ]
    )
    description = CharField(max_length=522)
    url_video = CharField(max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'teachers'


class Course(BaseModel):
    full_name = ForeignKey(Teacher, on_delete=PROTECT)
    image = ImageField(upload_to='icons/')
    title = CharField(max_length=255)
    duration = IntegerField()
    rating = FloatField(
        validators=[
            MaxValueValidator(5, 'Should be 5'),
            MinValueValidator(1, 'Should be 1')
        ]
    )
    description = CharField(max_length=522)
    category = ForeignKey(CourseCategory, on_delete=PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'courses'


class Student(BaseModel):
    full_name = CharField(max_length=255)
    image = ImageField(upload_to='icons/')
    course = ForeignKey(CourseCategory, on_delete=PROTECT)
    description = CharField(max_length=522)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'students'


class CourseNew(BaseModel):
    image = ImageField(upload_to='icons/')
    title = CharField(max_length=255)
    description = CharField(max_length=522)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'


class CourseComplain(BaseModel):
    first_name = CharField(max_length=255)
    phone_number = CharField(max_length=9, validators=[
        MaxValueValidator(9, 'Should be 9')
    ])
    description = CharField(max_length=522)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'complains'


class Customer(BaseModel):
    course = ForeignKey(CourseCategory, on_delete=PROTECT)
    first_name = CharField(max_length=255)
    phone_number = CharField(max_length=9, validators=[
        MaxValueValidator(9, 'Should be 9')
    ])

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'customers'
