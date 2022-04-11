from ast import Delete
from django.urls import path , include

from .views import *

app_name = 'patient'

#from . import views
urlpatterns = [
    path("", PatientListView.as_view(), name="list"),
    path("add/", PatientCreateView.as_view(), name="add"),
    path("<int:pk>/", PatientDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", PatientDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", PatientUpdateView.as_view(), name="update"),
]
