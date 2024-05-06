from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'creation_date', 'created_by')
    readonly_fields = ('creation_date', 'created_by')

admin.site.register(Ticket, TicketAdmin)
