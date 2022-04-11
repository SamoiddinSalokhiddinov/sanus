from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from common.department.models import *

class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        widgets = {            
            "title": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Title ")}),
            "department": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self):
        cd = self.cleaned_data

        self_id = self.instance.id
        title = cd.get("title")

        check_title= Speciality.objects.filter(title=title).exists()
        check_speciality = Speciality.objects.filter(id=self_id).exists()
       
  
        if check_speciality and check_title:
            self.add_error("title" , _("Speciality exists"))

        return cd
   