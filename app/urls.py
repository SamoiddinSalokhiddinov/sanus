from django.urls import path , include

#from . import views
urlpatterns = [
    path("", include("app.view.major.main.urls", namespace="main") , ),

    path("doctor/", include("app.view.major.doctor.urls", namespace="doctor"), ),
    path("patient/", include("app.view.major.patient.urls", namespace="patient"), ),
    path("admittance/", include("app.view.major.admittance.urls", namespace="admittance"), ),
    path("department/", include("app.view.major.department.urls", namespace="department"), ),
    path("speciality/", include("app.view.major.speciality.urls", namespace="speciality"), ),
    path("reception/", include("app.view.major.reception.urls", namespace="reception"), ),
    path("nurse/", include("app.view.major.nurse.urls", namespace="nurse"), ),
    path("staff/", include("app.view.major.staff.urls", namespace="staff"), ),
    path("room_floor/", include("app.view.major.room.urls", namespace="room"), ),
]
