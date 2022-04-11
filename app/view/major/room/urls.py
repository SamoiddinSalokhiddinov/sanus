from django.urls import path , include

from .views import *

app_name = 'room'

#from . import views
urlpatterns = [
    path("room/", RoomListView.as_view(), name="list"),
    path("room/add/", RoomCreateView.as_view(), name="add"),
    path("room/<int:pk>/", RoomDetailView.as_view(), name="single"),
    path("room/delete/<int:pk>/", RoomDeleteView.as_view(), name="delete"),
    path("room/update/<int:pk>/", RoomUpdateView.as_view(), name="update"),

    path("floor/", FloorListView.as_view(), name="floor_list"),
    path("floor/add/", FloorCreateView.as_view(), name="floor_add"),
    path("floor/<int:pk>/", FloorDetailView.as_view(), name="floor_single"),
    path("floor/delete/<int:pk>/", FloorDeleteView.as_view(), name="floor_delete"),
    path("floor/update/<int:pk>/", FloorUpdateView.as_view(), name="floor_update"),
]
