from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django import template
from common.hospital.models import Hospital

from common.department.models import Department
from common.department.models import Speciality

from applicationForm.models import District
from applicationForm.models import Region
from django.urls import reverse

from common.room.models import Floor, Room


register = template.Library()
# Create your models here.


GENDER = (
    (1, _("Male")),
    (2, _("Female"))
)
class Staff(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    middle_name = models.CharField(_("Middle name"), max_length=100)
    surname = models.CharField(_("Surname"), max_length=100)
    birthday = models.DateField(_("Birthday"))
    photo = models.ImageField(_("Photo"), upload_to="staff/", null=True , blank=True)
    email = models.EmailField(_("Email"), null=True)
    phone = models.CharField(_("Phone"), max_length=13)
    phone2 = models.CharField(_("Phone 2"), max_length=13, null=True)

    hospital = models.ForeignKey(Hospital, verbose_name=_("Hospital"), on_delete=models.CASCADE, related_name=("staff_hospital"))
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE, related_name="staff_department")
    post = models.CharField(_("Staff"), max_length=100)

    city = models.ForeignKey(Region, verbose_name=_("City / Region"), on_delete=models.CASCADE, related_name="staff_city" , null=True)
    district = models.ForeignKey(District, verbose_name=_("District"), on_delete=models.CASCADE, related_name="staff_district" , null=True)
    room = models.ForeignKey(Room, verbose_name=_("Room"), on_delete=models.CASCADE, related_name=("staff_room"))
    floor = models.ForeignKey(Floor, verbose_name=_("Floor"), on_delete=models.CASCADE, related_name=("staff_floor"))

    gender = models.IntegerField(choices=GENDER, verbose_name=_("Gender"), default=1)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)

    def get_absolute_url(self):
            return reverse('doctors:single', kwargs={"slug": self.name})

    def __str__(self):
        return self.name + " " + self.department.title

    @register.filter(name='gender_verbose')
    def gender_verbose(self):
        return dict(GENDER)[self.gender]

    @property
    def image_url(self):
        # "Returns the image url."
        return '%s%s' % (settings.HOST, self.photo) if self.photo else ''

    class Meta:
        verbose_name = _("Nurse / Orderly ")
        verbose_name_plural = _("Nurse / Orderly")