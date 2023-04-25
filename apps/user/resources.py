from import_export.fields import Field
from import_export.resources import ModelResource

from apps.user.models import Customer


class CustomerResource(ModelResource):
    course = Field(attribute='course__name', column_name='Kurs Nomi')
    first_name = Field(attribute='first_name', column_name='F.I.Sh')
    phone_number = Field(attribute='phone_number', column_name='Telefon Raqami')
    status = Field(attribute='status', column_name='Holati')

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'phone_number', 'status', 'course')
        export_order = ('id', 'first_name', 'phone_number', 'status', 'course')
