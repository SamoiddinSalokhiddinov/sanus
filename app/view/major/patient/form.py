from dataclasses import fields
from pydoc import Doc
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from common.patient.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        widgets = {
            "card_id": forms.NumberInput(attrs={"class": "form-control", "placeholder" : _("Enter Card ID ")},),
            "name": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Name ")}),
            "middle_name": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Middle Name ")}), 
            "surname": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Surname ")}),
            "birthday": DateInput(format=('%Y-%m-%d'), attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
            
            "passport_number": forms.NumberInput(attrs={"class": "form-control", "placeholder" : _("Enter Passport Number ")},),
            "passport_serial": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Passport Serial ")}),

            "email": forms.EmailInput(attrs={"class": "form-control" , "placeholder" : _("Enter Email ")}),
            "phone": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Phone ")}), 
            "phone2": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Phone 2 ")}),

            "work_place": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Work Place ")}),
            "city": forms.Select(attrs={"class": "form-control"}),
            "district": forms.Select(attrs={"class": "form-control"}),  
            
            "gender": forms.Select(attrs={"class": "form-control"}),
            "blood": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self):
        cd = self.cleaned_data

        self_id = self.instance.id
        passport_number = cd.get("passport_number")
        card_id = cd.get("card_id")

        check_passport_number = Patient.objects.filter(passport_number=passport_number).exists()
        check_patient = Patient.objects.filter(id=self_id).exists()
       
        check_cardId = Patient.objects.filter(card_id=card_id).exists()
  
        if check_cardId and not check_patient:
            self.add_error("card_id" , _("Card id exists"))

        if check_passport_number and not check_patient:
            self.add_error("passport_number" , _("This patient exists"))
     
        return cd
   