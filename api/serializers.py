from rest_framework import serializers
from common.doctor.models import Doctor

from common.patient.models import *
from common.timetable.models import Admittance, AdmittanceType
from datetime import datetime, timedelta, time
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AdmittanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmittanceType
        fields = ("color","title", "color_class")

class AdmittanceSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(read_only=True , source="patient.name")
    ad_type_title = serializers.CharField(read_only=True, source="admittance_type.title")
    ad_type_color = serializers.CharField(read_only=True, source="admittance_type.color")
    ad_type_color_class = serializers.CharField(read_only=True, source="admittance_type.color_class")
   
    class Meta:
        model = Admittance
        fields = ("id",
            "date","start_hour","end_hour","patient",
            "admittance_type","ad_type_title", "ad_type_color", "ad_type_color_class", "patient_name",
            "created_at" , )


    # def get_todayPatients(self,obj):
    #     today = obj.
    #     return obj.date


class DoctorSerializer(serializers.ModelSerializer):
    admittance_doctor = AdmittanceSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ("id" , "name" , "surname", "admittance_doctor", )