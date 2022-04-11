from django.urls import path , include

from .views import *

app_name = 'speciality'

#from . import views
urlpatterns = [
    path("", SpecialityListView.as_view(), name="list"),
    path("add/", SpecialityCreateView.as_view(), name="add"),
    path("<int:pk>/", SpecialityDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", SpecialityDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", SpecialityUpdateView.as_view(), name="update"),
]
