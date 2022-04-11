from django.urls import path , include

from .views import *

app_name = 'reception'

#from . import views
urlpatterns = [
    path("", ReceptionListView.as_view(), name="list"),
    path("add/", ReceptionCreateView.as_view(), name="add"),
    path("<int:pk>/", ReceptionDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", ReceptionDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", ReceptionUpdateView.as_view(), name="update"),
]
