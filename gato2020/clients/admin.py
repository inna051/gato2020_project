from django.contrib import admin
from .models import ImportantClient

@admin.register(ImportantClient)
class ImportantClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'image')

    list_filter = ('name', 'address')

    search_fields = ['name', 'address']

    ordering = ('name',)

    fieldsets = (
        ('Ключови клиенти', {
            'fields':
                ('name', 'address', 'image')
         }
        ),
    )

