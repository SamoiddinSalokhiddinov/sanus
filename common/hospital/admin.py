from django.contrib import admin

# Register your models here.
import common.hospital.models as model


admin.site.register(model.Hospital)
