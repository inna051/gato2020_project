from django.contrib import admin
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

    list_filter = ('name',)

    search_fields = ['name']

    ordering = ('name',)

    fieldsets = (
        ('Населени места', {
            'fields': ('name', 'latitude', 'longitude')
        }),
    )

