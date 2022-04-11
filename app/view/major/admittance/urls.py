from ast import Delete
from django.urls import path , include

from .views import *

app_name = 'admittance'

#from . import views
urlpatterns = [
    path("", AdmittanceListView.as_view(), name="list"),
    path("add/", AdmittanceCreateView.as_view(), name="add"),
    path("<int:pk>/", AdmittanceDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", AdmittanceDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", AdmittanceUpdateView.as_view(), name="update"),

    path("type/", AdmittanceTypeListView.as_view(), name="type_list"),
    path("type/add/", AdmittanceTypeCreateView.as_view(), name="type_add"),
    path("type/delete/<int:pk>/", AdmittanceTypeDeleteView.as_view(), name="type_delete"),
    path("type/update/<int:pk>/", AdmittanceTypeUpdateView.as_view(), name="type_update"),

]
