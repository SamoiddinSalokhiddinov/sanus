from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("patients/" , views.PatientListView.as_view(), name="patient_list"),
    path("doctors/" , views.DoctorListView.as_view(), name="doctor_list"),
    path("doctor/<int:pk>" , views.DoctorDetailView.as_view(), name="doctor_detail"),
]