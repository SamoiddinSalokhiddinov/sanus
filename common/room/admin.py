from django.contrib import admin
import common.room.models as model

admin.site.register(model.Room)
admin.site.register(model.Floor)