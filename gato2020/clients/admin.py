from django.contrib import admin
from .models import ImportantClient

@admin.register(ImportantClient)
class ImportantClientAdmin(admin.ModelAdmin):
    pass
