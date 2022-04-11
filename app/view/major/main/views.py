from django.shortcuts import render
from django.views.generic import ListView, DetailView

from common.doctor.models import Doctor
# Create your views here.

class MainView(ListView):
    template_name = 'major/index.html'
    context_object_name = 'main_list'
    queryset = Doctor.objects.all()

