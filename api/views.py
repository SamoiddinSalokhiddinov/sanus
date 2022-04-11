from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView
from api.serializers import *
from rest_framework import filters
from common.patient.models import Patient
from common.doctor.models import *
# Create your views here.

class PatientListView(ListAPIView):
    queryset = Patient.objects.all().order_by("-id")
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "surname" , "middle_name" , "card_id"]


class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()  
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "surname" ,"middle_name" , "card_id"]


class DoctorDetailView(RetrieveAPIView):
    queryset = Doctor.objects.all()  
    serializer_class = DoctorSerializer