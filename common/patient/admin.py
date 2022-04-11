from django.contrib import admin

from .models import *
#from nested_admin import NestedModelAdmin, NestedTabularInline

admin.site.register(Patient)


# class DoctorInline(NestedTabularInline):
#     model = Doctor
#     extra = 1

# class SpecialityInline(NestedTabularInline):
#     model = Speciality
#     inlines = [DoctorInline]

# @admin.register(Department)
# class DepartmentAdmin(NestedModelAdmin):
#     inlines = [SpecialityInline]
