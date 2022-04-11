from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from common.department.models import Department
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch

from django.contrib.messages.views import SuccessMessageMixin

from common.doctor.models import Doctor
from .form import *

class DepartmentListView(ListView):
    template_name = 'department/list.html'
    context_object_name = 'departments'
    queryset = Department.objects.all()


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/single.html'
    context_object_name = 'department'
    slug_field = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Department.objects.prefetch_related(
            Prefetch(
                "speciality_department",
                queryset = Speciality.objects.prefetch_related(
                    Prefetch(
                        "doctor_speciality",
                        queryset = Doctor.objects.filter(speciality=self.kwargs["pk"]),
                        to_attr="doctors"
                    )
                ),
                to_attr="specialities"
            )
        ).filter(id=self.kwargs['pk']).first()

        specialities = queryset.specialities
        for item in specialities:
            print(item.doctors)
       
      # print(specialities)

    #    queryset = Department.objects.prefetch_related(
    #         Prefetch(
    #             "speciality_department",
    #             queryset = Speciality.objects.filter(department=self.kwargs["pk"]),
    #             to_attr="specialities"
    #         )
    #     ).filter(id=self.kwargs['pk']).first()
        print(queryset.specialities)        
        context['specialities'] = specialities
        return context

class DepartmentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'department/form.html'
    context_object_name = 'data'
    form_class = DepartmentForm
    success_message = _('Department successfully added')
    success_url = reverse_lazy("department:list")


class DepartmentUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'department/form.html'
    model = Department
    form_class = DepartmentForm
    success_message =  _('Department successfully updated')
    success_url = reverse_lazy("department:list")

    def get_success_url(self):
        return reverse_lazy("department:list")

class DepartmentDeleteView(SuccessMessageMixin, DeleteView):
    model = Department
    success_url = reverse_lazy("department:list")
    success_message =  _('Department successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DepartmentDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
