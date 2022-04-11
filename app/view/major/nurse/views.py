from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin

from common.nurse.models import Nurse
from .form import *

class NurseListView(ListView):
    template_name = 'nurse/list.html'
    context_object_name = 'nurses'
    queryset = Nurse.objects.all()


class NurseDetailView(DetailView):
    model = Nurse
    template_name = 'nurse/single.html'
    context_object_name = 'nurse'
    slug_field = "pk"


class NurseCreateView(SuccessMessageMixin, CreateView):
    template_name = 'nurse/form.html'
    context_object_name = 'data'
    form_class = NurseForm
    success_message = _('Nurse successfully added')
    success_url = reverse_lazy("nurse:list")


class NurseUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'nurse/form.html'
    model = Nurse
    form_class = NurseForm
    success_message =  _('Nurse successfully updated')
    success_url = reverse_lazy("nurse:list")

    def get_success_url(self):
        return reverse_lazy("nurse:list")

class NurseDeleteView(SuccessMessageMixin, DeleteView):
    model = Nurse
    success_url = reverse_lazy("nurse:list")
    success_message =  _('Nurse successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(NurseDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
