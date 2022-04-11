from multiprocessing import context
from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from common.patient.models import Patient
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin
from .form import *

class PatientListView(ListView):
    template_name = 'patient/list.html'
    context_object_name = 'patients'
    queryset = Patient.objects.all()


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/single.html'
    context_object_name = 'patient'
    slug_field = "pk"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class PatientCreateView(SuccessMessageMixin, CreateView):
    template_name = 'patient/form.html'
    context_object_name = 'data'
    form_class = PatientForm
    success_message = _('Patient successfully added')
    success_url = reverse_lazy("patient:list")


class PatientUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'patient/form.html'
    model = Patient
    form_class = PatientForm
    success_message =  _('Patient successfully updated')
    success_url = reverse_lazy("patient:list")

    def get_success_url(self):
        return reverse_lazy("patient:list")

class PatientDeleteView(SuccessMessageMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy("patient:list")
    success_message =  _('Patient successfully deleted')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PatientDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)




# class NewsView(ListView):
#     template_name = 'admin_temp/news/index.html'
#     context_object_name = 'news_list'
#     queryset = News.objects.all()


# class NewsCreateView(SuccessMessageMixin, CreateView):
#     template_name = 'admin_temp/news/create.html'
#     context_object_name = 'news'
#     form_class = NewsForm
#     success_message = 'News successfully added'
#     success_url = reverse_lazy("news")


# class NewsUpdateView(SuccessMessageMixin, UpdateView):
#     model = News
#     slug_field = "pk"
#     template_name = "admin_temp/news/update.html"
#     success_message = 'News successfully updated'
#     context_object_name = 'news'
#     form_class = NewsForm

#     def get_success_url(self):
#         return reverse('news')


# class NewsDeleteView(SuccessMessageMixin, DeleteView):
#     model = News
#     success_url = reverse_lazy("news")
#     success_message = 'News successfully deleted'

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_message)
#         return super(NewsDeleteView, self).delete(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)