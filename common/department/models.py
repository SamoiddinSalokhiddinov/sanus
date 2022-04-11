from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.hospital.models import Hospital

# Department

class Department(models.Model):
    title = models.CharField(_("Title"),  max_length=100)
    hospital = models.ForeignKey(Hospital, verbose_name=_("Hospital"), on_delete=models.CASCADE, related_name="department_hospital")

    def __str__(self):
        return self.title
   
    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class Speciality(models.Model):
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE, related_name="speciality_department")
    title = models.CharField(_("Title"),  max_length=100)


    def __str__(self):
            return self.title
   
    class Meta:
        verbose_name = _("Speciality")
        verbose_name_plural = _("Specialities")
