from dataclasses import fields
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from pkg_resources import require
from common.timetable.models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class DateInput(forms.DateInput):
    input_type = 'date'


class AdmittanceTypeForm(forms.ModelForm):
    class Meta:
        model = AdmittanceType
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        widgets = {
            "doctor": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class":"form-control", "placeholder": _("Enter Title")}),
            "duration": forms.NumberInput(attrs={"class": "form-control"}),
        }



class AdmittanceForm(forms.ModelForm):
    class Meta:
        model = Admittance
        fields = "__all__"
        exclude = ['created_at', 'updated_at',]
        widgets = {
            "date" : DateInput(format=('%Y-%m-%d'), attrs={"class": "form-control"}),
            "start_hour": forms.TimeInput(attrs={"class" : "form-control" , "type" : "time"}),
            "end_hour": forms.TimeInput(attrs={"class" : "form-control" , "type" : "time"}),
            "doctor" : forms.Select(attrs={"class": "form-control"} ),
            "status" : forms.Select(attrs={"class": "form-control"} ),
            "patient" : forms.Select(attrs={"class": "form-control" ,}),
            "admittance_type" : forms.Select(attrs={"class": "form-control"}),
            "symptoms" : forms.SelectMultiple(attrs={"class": "select2 form-select"}),
            'diagnosis': forms.CharField(widget=CKEditorWidget()),
            'extra_file': forms.FileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(self["symptoms"])
    
    

class AdmittingForm(forms.ModelForm):
    #  new_sympotms = forms.TextInput(attrs={"class": "form-control" ,"readonly": True , }),
    # original_field = forms.CharField()
    # extra_field_count = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Admittance
        fields = "__all__"
        exclude = ['created_at', 'updated_at',]
        widgets = {
            "date" : DateInput(format=('%Y-%m-%d'), attrs={"class": "form-control","readonly": True } ),
            "start_hour": forms.TimeInput(attrs={"class" : "form-control" , "type" : "time","readonly": True ,}),
            "end_hour": forms.TimeInput(attrs={"class" : "form-control" , "type" : "time","readonly": True ,}),
            "doctor" : forms.TextInput(attrs={"class": "form-control","readonly": True ,}, ),
            "status" : forms.Select(attrs={"class": "form-control"} ),
            "patient" : forms.TextInput(attrs={"class": "form-control" ,"readonly": True ,}),
            "admittance_type" : forms.Select(attrs={"class": "form-control","readonly": True}),
            "symptoms" : forms.SelectMultiple(attrs={"class": "select2 form-select"}),
            'diagnosis': forms.CharField(widget=CKEditorWidget()),
            'extra_file': forms.FileInput(attrs={"class": "form-control"}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["symptoms"].queryset = Symptoms.objects.filter(doctor=self.instance.doctor)

        # extra_fields = kwargs.pop('extra', 0)
        # print(extra_fields)
        
        # self.fields['extra_field_count'].initial = extra_fields

        # for index in range(int(extra_fields)):
        #     self.fields['extra_field_{index}'.format(index=index)] = forms.TextInput(attrs={"class": "form-control" ,"readonly": True}),

  

class BaseArticleFormSet(forms.BaseFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["my_field"] = forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Title ")}), 

class SymptomsForm(forms.ModelForm):
    class Meta:
        model = Symptoms
        fields = "__all__"
        exclude = ['created_at', 'updated_at' ,]
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control", "placeholder": _("Enter Title")}),
            "doctor" : forms.TextInput(attrs={"class": "form-control","readonly": True}, ),

        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(kwargs.get(''))
    #     self.fields["doctor"].queryset = self.instance.doctor
        