from django.urls import path , include

from .views import *

app_name = 'nurse'

#from . import views
urlpatterns = [
    path("", NurseListView.as_view(), name="list"),
    path("add/", NurseCreateView.as_view(), name="add"),
    path("<int:pk>/", NurseDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", NurseDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", NurseUpdateView.as_view(), name="update"),
]
