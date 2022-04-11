import datetime
from django.http import request , HttpResponse , HttpResponseRedirect, HttpRequest
from multiprocessing import context
from pyexpat import model
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from django.db.models import Prefetch

from common.doctor.models import Doctor
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin

from common.timetable.models import Schedule, Timetable
from .form import *

class DoctorListView(ListView):
    template_name = 'doctor/list.html'
    context_object_name = 'doctors'
    queryset = Doctor.objects.all()


class DoctorDetailView(SuccessMessageMixin, DetailView):
    model = Doctor
    template_name = 'doctor/single.html'
    context_object_name = 'doctor'
    slug_field = "pk"

    def post(self, request , pk):
        print(request)
        form = AdmittanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Admittance added"))
            return HttpResponseRedirect(reverse_lazy("doctor:single" , kwargs={"pk" : pk}))
        else:
            form = AdmittanceForm()
            return HttpResponseRedirect(reverse_lazy("doctor:list"))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print("rad0" ,datetime.today() , datetime.now().date())
        form = AdmittanceForm()
        queryset = Doctor.objects.prefetch_related(
             Prefetch(
                "admittance_type_doctor",
                queryset = AdmittanceType.objects.filter(doctor=self.kwargs["pk"]),
                to_attr="admittance_types"
            )
        ).prefetch_related(
            Prefetch(
                "admittance_doctor",
                queryset = Admittance.objects.filter(doctor=self.kwargs["pk"], date=datetime.now().date()).order_by("id"),
                to_attr="admittances"
            )
        ).filter(id=self.kwargs['pk']).first()
        admittance_types = queryset.admittance_types
        admittances = queryset.admittances


        context["admittance_types"] = admittance_types
        context["form"] = form
        context["admittances"] = admittances

        return context

class DoctorCreateView(SuccessMessageMixin, CreateView):
    template_name = 'doctor/form.html'
    context_object_name = 'data'
    form_class = DoctorForm
    success_message = _('Doctor successfully added')
    success_url = reverse_lazy("doctor:list")


class DoctorUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'doctor/form.html'
    model = Doctor
    form_class = DoctorForm
    success_message =  _('Doctor successfully updated')
    success_url = reverse_lazy("doctor:list")

    def get_success_url(self):
        return reverse_lazy("doctor:list")

class DoctorDeleteView(SuccessMessageMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy("doctor:list")
    success_message =  _('Doctor successfully deleted')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DoctorDeleteView , self).delete(request, *args, **kwargs)

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