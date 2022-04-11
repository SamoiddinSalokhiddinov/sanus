import datetime
import email


from distutils.command.upload import upload
from django.conf import settings
from tabnanny import verbose
from django.utils import timezone

from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

from applicationForm.models import District
from applicationForm.models import Region

# HOSPITAL 

class Hospital(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=200)
    logo = models.ImageField(_("Logo"), upload_to="hospital/", null=True , blank=True)

    location = models.URLField(_("Location"), null=True)
    city = models.ForeignKey(Region, verbose_name=_("City / Region"), on_delete=models.CASCADE, related_name="hospital_city")
    district = models.ForeignKey(District, verbose_name=_("District"), on_delete=models.CASCADE, related_name="hospital_district")
    
    phone = models.CharField(_("Phone"), max_length=100 , null=True)
    phone2 = models.CharField(_("Phone 2"), max_length=100 , null=True) 
    email = models.EmailField(_("Email"), null=True)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)


    def get_absolute_url(self):
            return reverse('hospital', kwargs={"slug": self.title})

    def __str__(self):
        return self.title

   
    @property
    def image_url(self):
        # "Returns the image url."
        return '%s%s' % (settings.HOST, self.logo) if self.logo else ''

    class Meta:
        verbose_name = _("Hospital")
        verbose_name_plural = _("Hospitals")