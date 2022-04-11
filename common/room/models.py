from math import floor
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

class Floor(models.Model):
    floor = models.IntegerField(_("Floor"))

    def __str__(self):
        return _("Floor") + " : " + str(self.floor)

    class Meta:
        verbose_name = _("Floor")
        verbose_name_plural = _("Floor")

class Room(models.Model):
    floor = models.ForeignKey(Floor, verbose_name=_("Floor"), on_delete=models.CASCADE, related_name=("room_floor"))
    room = models.IntegerField(_("Room"))

    def __str__(self):
        return   _("Floor") + " : " + str(self.floor.floor) + " " +  _("Room") + " : " + str(self.room)
        
    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Room")