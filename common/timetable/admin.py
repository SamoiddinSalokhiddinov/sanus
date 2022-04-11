from dataclasses import fields
from django.contrib import admin
from .models import *
from datetime import datetime , time
from django.utils.translation import gettext_lazy as _


# Register your models here.
# admin.site.register(Schedule)
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("date","start_hour","end_hour","doctor","work_hour")
    fields = ("date","start_hour","end_hour","doctor","work_hour","patient")
    readonly_fields = ("work_hour",)
    

    def work_hour(self, obj):
        if obj.end_hour :
            end_hour = datetime.combine(datetime.now(), obj.end_hour)
            start_hour = datetime.combine(datetime.now(), obj.start_hour)
            diff = end_hour - start_hour
            return diff
        else :    
            return _("Not given yet")
      


admin.site.register(Timetable)
admin.site.register(Admittance) 
admin.site.register(AdmittanceType) 
admin.site.register(Symptoms) 