from django.urls import path , include

from .views import *

app_name = 'department'

#from . import views
urlpatterns = [
    path("", DepartmentListView.as_view(), name="list"),
    path("add/", DepartmentCreateView.as_view(), name="add"),
    path("<int:pk>/", DepartmentDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", DepartmentDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", DepartmentUpdateView.as_view(), name="update"),
]
