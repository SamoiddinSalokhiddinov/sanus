from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin

from common.reception.models import Receptionist
from .form import *

class ReceptionListView(ListView):
    template_name = 'reception/list.html'
    context_object_name = 'receptionists'
    queryset = Receptionist.objects.all()


class ReceptionDetailView(DetailView):
    model = Receptionist
    template_name = 'reception/single.html'
    context_object_name = 'receptionist'
    slug_field = "pk"


class ReceptionCreateView(SuccessMessageMixin, CreateView):
    template_name = 'reception/form.html'
    context_object_name = 'data'
    form_class = ReceptionForm
    success_message = _('Reception successfully added')
    success_url = reverse_lazy("reception:list")


class ReceptionUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'reception/form.html'
    model = Receptionist
    form_class = ReceptionForm
    success_message =  _('Reception successfully updated')
    success_url = reverse_lazy("reception:list")

    def get_success_url(self):
        return reverse_lazy("reception:list")

class ReceptionDeleteView(SuccessMessageMixin, DeleteView):
    model = Receptionist
    success_url = reverse_lazy("reception:list")
    success_message =  _('Reception successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReceptionDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
