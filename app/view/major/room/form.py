from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from common.room.models import *

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        widgets = {            
            "floor": forms.NumberInput(attrs={"class": "form-control" , "placeholder" : _("Enter room ")}),
        }

    def clean(self):
        cd = self.cleaned_data

        self_id = self.instance.id
        floor = cd.get("floor")

        check_room= Floor.objects.filter(floor=floor).exists()
        check_exist = Floor.objects.filter(id=self_id).exists()
  
        if check_room and not check_exist:
            self.add_error("floor" , _("Floor exists"))

        return cd
   

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        widgets = {            
            "room": forms.NumberInput(attrs={"class": "form-control" , "placeholder" : _("Enter room ")}),
            "floor": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self):
        cd = self.cleaned_data

        self_id = self.instance.id
        room = cd.get("room")
        floor = cd.get("floor")

        check_room= Room.objects.filter(room=room, floor=floor).exists()
        check_exist = Room.objects.filter(id=self_id).exists()
  
        if check_room and not check_exist:
            self.add_error("room" , _("Room exists"))

        return cd
   