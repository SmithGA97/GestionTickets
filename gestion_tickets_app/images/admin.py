from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'created_by')
    readonly_fields = ('created_by',)

    def created_by(self, obj):
        return obj.ticket_id.created_by

    created_by.short_description = 'created by'
admin.site.register(Image, ImageAdmin)
