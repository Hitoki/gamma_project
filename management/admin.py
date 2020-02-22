from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Shop)
admin.site.register(models.Staff)
admin.site.register(models.Schedule)
admin.site.register(models.Cost)
admin.site.register(models.Cost_type)
admin.site.register(models.ActivityLog)
admin.site.register(models.User)
