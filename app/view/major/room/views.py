from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from common.room.models import Room , Floor
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin

from .form import *


class FloorListView(ListView):
    template_name = 'floor/list.html'
    context_object_name = 'floors'
    queryset = Floor.objects.all()


class FloorDetailView(DetailView):
    model = Floor
    template_name = 'floor/single.html'
    context_object_name = 'floor'
    slug_field = "pk"

   

class FloorCreateView(SuccessMessageMixin, CreateView):
    template_name = 'floor/form.html'
    context_object_name = 'data'
    form_class = FloorForm
    success_message = _('Floor successfully added')
    success_url = reverse_lazy("room:floor_list")


class FloorUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'floor/form.html'
    model = Floor
    form_class = FloorForm
    success_message =  _('Floor successfully updated')
    success_url = reverse_lazy("room:floor_list")

    def get_success_url(self):
        return reverse_lazy("room:floor_list")

class FloorDeleteView(SuccessMessageMixin, DeleteView):
    model = Floor
    success_url = reverse_lazy("room:floor_list")
    success_message =  _('Floor successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(FloorDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    




class RoomListView(ListView):
    template_name = 'room/list.html'
    context_object_name = 'rooms'
    queryset = Room.objects.all()

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room/single.html'
    context_object_name = 'room'
    slug_field = "pk"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     queryset = Room.objects.prefetch_related(
    #          Prefetch(
    #             "doctor_room",
    #             queryset = Doctor.objects.filter(room=self.kwargs["pk"]),
    #             to_attr="doctors"
    #         )
    #     ).filter(id=self.kwargs['pk']).first()

    #     doctors = queryset.doctors
    #     context["doctors"] = doctors
    #     return context

class RoomCreateView(SuccessMessageMixin, CreateView):
    template_name = 'room/form.html'
    context_object_name = 'data'
    form_class = RoomForm
    success_message = _('Room successfully added')
    success_url = reverse_lazy("room:list")


class RoomUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'room/form.html'
    model = Room
    form_class = RoomForm
    success_message =  _('Room successfully updated')
    success_url = reverse_lazy("room:list")

    def get_success_url(self):
        return reverse_lazy("room:list")

class RoomDeleteView(SuccessMessageMixin, DeleteView):
    model = Room
    success_url = reverse_lazy("room:list")
    success_message =  _('Room successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RoomDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
