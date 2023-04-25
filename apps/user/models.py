from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CharField, SlugField, ImageField, ForeignKey, CASCADE, CASCADE, FloatField, IntegerField, \
    TextChoices, URLField
from django.utils.text import slugify

from apps.shared.models import BaseModel


class CourseCategory(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)
    photo = ImageField(upload_to='icons/')

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while CourseCategory.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Teacher(BaseModel):
    full_name = CharField(max_length=255)
    direction = ForeignKey(CourseCategory, on_delete=CASCADE)
    image = ImageField(upload_to='icons/')
    rating = FloatField(
        validators=[
            MaxValueValidator(5, 'Should be 5'),
            MinValueValidator(1, 'Should be 1')
        ]
    )
    description = CharField(max_length=522)
    url_video = URLField()

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'teachers'


class Course(BaseModel):
    full_name = ForeignKey(Teacher, on_delete=CASCADE)
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
    category = ForeignKey(CourseCategory, on_delete=CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'courses'


class Student(BaseModel):
    full_name = CharField(max_length=255)
    image = ImageField(upload_to='icons/')
    course = ForeignKey(CourseCategory, on_delete=CASCADE)
    teacher = ForeignKey(Teacher, on_delete=CASCADE)
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
    phone_number = CharField(max_length=25)
    description = CharField(max_length=522)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'complains'


class Customer(BaseModel):
    class Status(TextChoices):
        INACTIVE = "Kutilyapti"
        ACTIVE = "Qabul qilindi"
        REJECT = "Qabul qilinmadi"
        POSTPONED = "Keyinroqqa qo'yildi"

    course = ForeignKey(CourseCategory, on_delete=CASCADE)
    first_name = CharField(max_length=255)
    phone_number = CharField(max_length=25)
    status = CharField(max_length=25, choices=Status.choices, default=Status.INACTIVE)

    class Meta:
        db_table = 'customers'
