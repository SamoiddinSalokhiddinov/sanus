from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django import template
register = template.Library()
from applicationForm.models import District
from applicationForm.models import Region



GENDER = (
    (1, _("Male")),
    (2, _("Female"))
)

BLOOD = (
    (1 , _("(A+) A RhD positive")),
    (2 , _("(A-) A RhD negative")),
    (3 , _("(B+) B RhD positive")),
    (4 , _("(B-) B RhD negative")),
    (5 , _("(O+) O RhD positive")),
    (6 , _("(O-) O RhD negative")),
    (7 , _("(AB+) AB RhD positive")),
    (8 , _("(AB-) AB RhD negative")),
)

# Create your models here.
class Patient(models.Model):
    card_id = models.PositiveIntegerField(_("ID Card"), null=True)
    name = models.CharField(_("Name"), max_length=20)
    middle_name = models.CharField(_("Middle name"), max_length=25)
    surname = models.CharField(_("Surname"), max_length=25)
    birthday = models.DateField(_("Birthday"))
    photo = models.ImageField(_("Photo"), upload_to="patient/", null=True , blank=True)

    passport_serial = models.CharField(_("Passport Serial"), max_length=2)
    passport_number = models.IntegerField(_("Passport Number"))

    email = models.EmailField(_("Email"), null=True)
    phone = models.CharField(_("Phone"), max_length=13)
    phone2 = models.CharField(_("Phone 2"), max_length=13, null=True)
    work_place = models.CharField(_("Work Place"), max_length=255, null=True)

    city = models.ForeignKey(Region, verbose_name=_("City / Region"), on_delete=models.CASCADE, related_name="patient_city", null=True ,)
    district = models.ForeignKey(District, verbose_name=_("District"), on_delete=models.CASCADE, related_name="patient_district", null=True ,)

    gender = models.IntegerField(choices=GENDER, verbose_name=_("Gender"), default=1)
    blood = models.IntegerField(choices=BLOOD, verbose_name=_("Blood"), default=1)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)
   
    @register.filter(name='blood_verbose')
    def blood_verbose(self):
        return dict(BLOOD)[self.blood]

   
    def get_absolute_url(self):
            return reverse('patient', kwargs={"slug": self.name})

    def __str__(self):
        return self.name

 
    @property
    def image_url(self):
        # "Returns the image url."
        return '%s%s' % (settings.HOST, self.photo) if self.photo else ''

    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")