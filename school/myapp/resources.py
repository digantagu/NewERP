from import_export import resources
from .models import Student


class BulkStudent(resources.ModelResource):
    class Meta:
        model = Student
