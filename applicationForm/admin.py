from django.contrib import admin

# Register your models here.
import applicationForm.models as model


admin.site.register(model.Region)
admin.site.register(model.District)
admin.site.register(model.Role)
admin.site.register(model.BaseUser)
admin.site.register(model.UserRole)
