from dataclasses import fields
from pydoc import Doc
from traceback import print_tb
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from common.reception.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = "__all__"
        exclude = ['created_at', 'updated_at', 'city' , 'district']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Name ")}),
            "middle_name": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Middle Name ")}), 
            "surname": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Surname ")}),
            "birthday": DateInput(format=('%Y-%m-%d'), attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
          
            "email": forms.EmailInput(attrs={"class": "form-control" , "placeholder" : _("Enter Email ")}),
            "phone": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Phone ")}), 
            "phone2": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Phone 2 ")}),
            "hospital": forms.Select(attrs={"class": "form-control"}),

            "city": forms.Select(attrs={"class": "form-control"}),
            "district": forms.Select(attrs={"class": "form-control"}),  
            
            "gender": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self):
        cd = self.cleaned_data
        print(cd)
        self_id = self.instance.id
        email = cd.get("email")
        print(email)
        check_email = Receptionist.objects.filter(email=email).exists()
        check_receptionist = Receptionist.objects.filter(id=self_id).exists()
       
        if check_email and not check_receptionist:
            self.add_error("email" , _("This email exists"))
     
        return cd
   