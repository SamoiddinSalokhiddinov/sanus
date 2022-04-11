from traceback import print_tb
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from common.nurse.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
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
            "department": forms.Select(attrs={"class": "form-control"}),
            "post": forms.Select(attrs={"class": "form-control"}),
            "hospital": forms.Select(attrs={"class": "form-control"}),

            "city": forms.Select(attrs={"class": "form-control"}),
            "district": forms.Select(attrs={"class": "form-control"}),  
            "nurse": forms.Select(attrs={"class": "form-control"}),
            "floor": forms.Select(attrs={"class": "form-control"}),  
            
            
            "gender": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self):
        cd = self.cleaned_data
        print(cd)
        self_id = self.instance.id
        email = cd.get("email")
        print(email)
        check_email = Nurse.objects.filter(email=email).exists()
        check_Nurse = Nurse.objects.filter(id=self_id).exists()
       
        if check_email and not check_Nurse:
            self.add_error("email" , _("This email exists"))
     
        return cd
   