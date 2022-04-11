from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin

from common.staff.models import Staff
from .form import *

class StaffListView(ListView):
    template_name = 'staff/list.html'
    context_object_name = 'staffs'
    queryset = Staff.objects.all()


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'staff/single.html'
    context_object_name = 'staff'
    slug_field = "pk"


class StaffCreateView(SuccessMessageMixin, CreateView):
    template_name = 'staff/form.html'
    context_object_name = 'data'
    form_class = StaffForm
    success_message = _('Staff successfully added')
    success_url = reverse_lazy("staff:list")


class StaffUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'staff/form.html'
    model = Staff
    form_class = StaffForm
    success_message =  _('Staff successfully updated')
    success_url = reverse_lazy("staff:list")

    def get_success_url(self):
        return reverse_lazy("staff:list")

class StaffDeleteView(SuccessMessageMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy("staff:list")
    success_message =  _('Staff successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StaffDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
