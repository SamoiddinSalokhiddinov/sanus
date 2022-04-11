from multiprocessing import context
from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from common.timetable.models import AdmittanceType , Admittance
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin
from .form import *


# ADMITANCE TYPE VIEW

class AdmittanceTypeListView(ListView):
    template_name = 'admittance_type/list.html'
    context_object_name = 'admittances'
    queryset = AdmittanceType.objects.all()

class AdmittanceTypeDetailView(DetailView):
    model = AdmittanceType
    template_name = 'admittance/single.html'
    context_object_name = 'admittance'
    slug_field = "pk"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class AdmittanceTypeCreateView(SuccessMessageMixin, CreateView):
    template_name = 'admittance_type/form.html'
    context_object_name = 'data'
    form_class = AdmittanceTypeForm
    success_message = _('AdmittanceType successfully added')
    success_url = reverse_lazy("admittance:type_list")


class AdmittanceTypeUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'admittance_type/form.html'
    model = AdmittanceType
    form_class = AdmittanceTypeForm
    success_message =  _('AdmittanceType successfully updated')
    success_url = reverse_lazy("admittance:type_list")

    def get_success_url(self):
        return reverse_lazy("admittance:type_list")

class AdmittanceTypeDeleteView(SuccessMessageMixin, DeleteView):
    model = AdmittanceType
    success_url = reverse_lazy("admittance:type_list")
    success_message =  _('AdmittanceType successfully deleted')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdmittanceDeleteView , self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
         return self.post(request, *args, **kwargs)


# END ADMITTANCE TYPE VIEW 


# ADMITANCE VIEW

class AdmittanceListView(ListView):
    template_name = 'admittance/list.html'
    context_object_name = 'admittances'
    queryset = Admittance.objects.all()


class AdmittanceDetailView(DetailView):
    model = Admittance
    template_name = 'admittance/single.html'
    context_object_name = 'admittance'
    slug_field = "pk"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class AdmittanceCreateView(SuccessMessageMixin, CreateView):
    template_name = 'admittance/form.html'
    context_object_name = 'data'
    form_class = AdmittanceForm
    success_message = _('Admittance successfully added')
    success_url = reverse_lazy("admittance:list")


class AdmittanceUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'admittance/form.html'
    model = Admittance
    form_class = AdmittanceForm
    success_message =  _('Admittance successfully updated')
    success_url = reverse_lazy("admittance:list")

    def get_success_url(self):
        return reverse_lazy("admittance:list")

class AdmittanceDeleteView(SuccessMessageMixin, DeleteView):
    model = Admittance
    success_url = reverse_lazy("admittance:list")
    success_message =  _('Admittance successfully deleted')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdmittanceDeleteView , self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
         return self.post(request, *args, **kwargs)


# END ADMITTANCE VIEW 