
from datetime import date , datetime
from tokenize import blank_re
from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from common.doctor.models import Doctor
from common.patient.models import Patient
from datetime import datetime, timedelta, time
from ckeditor.fields import RichTextField

COLORS = (
    ( "#0d6efd", "primary"),
    ( "#dc3545", "danger"),
    ( "#6c757d", "secondary"),
    ( "#198754", "success"),
    ( "#ffc107", "warning"),
    ( "#f8f9fa", "light"),
    ( "#212529", "dark"),
)

STATUS = (
    ( "waiting", _("Waiting")),
    ( "admitting", _("Admitting")),
    ( "admitted", _("Admitted")),
)
GENDER = (
    (1, _("Male")),
    (2, _("Female"))
)
gender = models.IntegerField(choices=GENDER, verbose_name=_("Gender"), default=1)

class Timetable(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="timetable_doctor")
    
    monday_start = models.TimeField(verbose_name=_("(Monday) Start Hour"), blank=True)
    monday_end = models.TimeField(verbose_name=_("(Monday) End Hour"), blank=True)

    tuesday_start = models.TimeField(verbose_name=_("(Tuesday) Start Hour"), blank=True)
    tuesday_end = models.TimeField(verbose_name=_("(Tuesday) End Hour"), blank=True)

    wednesday_start = models.TimeField(verbose_name=_("(Wednesday) Start Hour"), blank=True)
    wednesday_end = models.TimeField(verbose_name=_("(Wednesday) End Hour"), blank=True)
    
    thursday_start = models.TimeField(verbose_name=_("(Thursday) Start Hour"), blank=True)
    thursday_end = models.TimeField(verbose_name=_("(Thursday) End Hour"), blank=True)

    friday_start = models.TimeField(verbose_name=_("(Friday) Start Hour"), blank=True)
    friday_end = models.TimeField(verbose_name=_("(Friday) End Hour"), blank=True)

    saturday_start = models.TimeField(verbose_name=_("(Saturday) Start Hour"), blank=True)
    saturday_end = models.TimeField(verbose_name=_("(Saturday) End Hour"), blank=True)

    sunday_start = models.TimeField(verbose_name=_("(Sunday) Start Hour"), blank=True)
    sunday_end = models.TimeField(verbose_name=_("(Sunday) End Hour"), blank=True)

    

    class Meta:
        verbose_name = _("Timetable")
        verbose_name_plural = _("Timetables")

class Schedule(models.Model):
    date = models.DateField(_("Date"), null=True)
    start_hour = models.TimeField(verbose_name=_("Start Hour"),blank=True,)
    end_hour = models.TimeField(verbose_name=_("End Hour"),blank=True,)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="schedule_doctor")
    patient = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE, related_name="schedule_patient", blank=True, null=True)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)


    def __str__(self):
        return self.doctor.name + " " + self.doctor.surname + " : " + str(self.date)

    @property
    def work_hour(self):
        end_hour = datetime.combine(datetime.now(), self.end_hour)
        start_hour = datetime.combine(datetime.now(), self.start_hour)
        diff = end_hour - start_hour
        return diff

    class Meta:
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedules")
   
class AdmittanceType(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="admittance_type_doctor")
    title = models.CharField(_("Title"), max_length=100)
    #color_class = models.CharField(_("Color class"), max_length=100 , blank=True)
    color = models.CharField(choices=COLORS, verbose_name=_("Colors"), default=COLORS, max_length=100)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)

    def __str__(self):
            return self.title

    @property
    def color_class(self):
        return self.get_color_display

    class Meta:
        verbose_name = _("Admittance Type")
        verbose_name_plural = _("Admittance Types")


class Symptoms(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="symptoms_doctor")
    title = models.CharField(_("Title"), max_length=100)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = _("Symptoms")
        verbose_name_plural = _("Symptoms")

class Admittance(models.Model):
    date = models.DateField(_("Date"), null=True)
    start_hour = models.TimeField(verbose_name=_("Start Hour"),blank=True,)
    end_hour = models.TimeField(verbose_name=_("End Hour"),blank=True,)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="admittance_doctor")
    patient = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE, related_name="admittance_patient",)
    admittance_type = models.ForeignKey(AdmittanceType, verbose_name=_("Admittance Type"), on_delete=models.CASCADE, related_name="adminttance_its_type")
    status = models.CharField(choices=STATUS, verbose_name=_("Status"), default=STATUS[0], max_length=100)
    symptoms = models.ManyToManyField(Symptoms, verbose_name=_("Symptoms"),  blank=True)
    diagnosis = RichTextField(blank=True,null=True)
    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)
    extra_file = models.FileField(_("Extra file"), upload_to="doctors/", null=True , blank=True)

    def __str__(self):
        return "Dr " + self.doctor.surname + " : " + "Patient " + self.patient.surname + " Hour : " + str(self.start_hour )

    @property
    def work_hour(self):
        end_hour = datetime.combine(datetime.now(), self.end_hour)
        start_hour = datetime.combine(datetime.now(), self.start_hour)
        diff = end_hour - start_hour
        return diff

    def get_today_patient(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        print(self.filter(start__lte=today_end, end__gte=today_start))
        return self.filter(start__lte=today_end, end__gte=today_start)
    class Meta:
        ordering = ['-id']  
        verbose_name = _("Admittance")
        verbose_name_plural = _("Admittances")

   