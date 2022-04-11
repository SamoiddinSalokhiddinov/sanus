import common.department.models as model

from django.contrib import admin

from .models import *
from common.doctor.models import Doctor

from nested_admin import NestedModelAdmin, NestedTabularInline

# admin.site.register(model.Department)
admin.site.register(model.Speciality)


class DoctorInline(NestedTabularInline):
    model = Doctor
    extra = 1

class SpecialityInline(NestedTabularInline):
    model = Speciality
    inlines = [DoctorInline]

@admin.register(Department)
class DepartmentAdmin(NestedModelAdmin):
    inlines = [SpecialityInline]


