from django.urls import path , include

from .views import *

app_name = 'staff'

#from . import views
urlpatterns = [
    path("", StaffListView.as_view(), name="list"),
    path("add/", StaffCreateView.as_view(), name="add"),
    path("<int:pk>/", StaffDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", StaffDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", StaffUpdateView.as_view(), name="update"),
]
