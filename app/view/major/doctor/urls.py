from ast import Delete
from django.urls import path , include

from .views import *

app_name = 'doctor'

#from . import views
urlpatterns = [
    path("", DoctorListView.as_view(), name="list"),
    path("add/", DoctorCreateView.as_view(), name="add"),
    path("<int:pk>/", DoctorDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", DoctorDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", DoctorUpdateView.as_view(), name="update"),
    #path("doctors", include("app.view.major.doctor.urls")),
    # path("nomination/create/", login_required(views.NominationCreateView.as_view()), name="nomination-create"),
    # path("nomination/<int:pk>/", login_required(views.NominationUpdateView.as_view()), name="nomination-update"),
    # path("nomination/delete/<int:pk>/", login_required(views.NominationDeleteView.as_view()), name="nomination-delete"),
]
