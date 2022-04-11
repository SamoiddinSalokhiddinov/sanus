from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from common.department.models import Speciality
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch

from django.contrib.messages.views import SuccessMessageMixin

from common.doctor.models import Doctor
from .form import *

class SpecialityListView(ListView):
    template_name = 'speciality/list.html'
    context_object_name = 'specialities'
    queryset = Speciality.objects.all()


class SpecialityDetailView(DetailView):
    model = Speciality
    template_name = 'speciality/single.html'
    context_object_name = 'speciality'
    slug_field = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Speciality.objects.prefetch_related(
             Prefetch(
                "doctor_speciality",
                queryset = Doctor.objects.filter(speciality=self.kwargs["pk"]),
                to_attr="doctors"
            )
        ).filter(id=self.kwargs['pk']).first()

        doctors = queryset.doctors
        context["doctors"] = doctors
        return context

class SpecialityCreateView(SuccessMessageMixin, CreateView):
    template_name = 'speciality/form.html'
    context_object_name = 'data'
    form_class = SpecialityForm
    success_message = _('Speciality successfully added')
    success_url = reverse_lazy("speciality:list")


class SpecialityUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'speciality/form.html'
    model = Speciality
    form_class = SpecialityForm
    success_message =  _('Speciality successfully updated')
    success_url = reverse_lazy("speciality:list")

    def get_success_url(self):
        return reverse_lazy("speciality:list")

class SpecialityDeleteView(SuccessMessageMixin, DeleteView):
    model = Speciality
    success_url = reverse_lazy("speciality:list")
    success_message =  _('Speciality successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SpecialityDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
