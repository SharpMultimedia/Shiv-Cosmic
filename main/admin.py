from django.contrib import admin
from .models import *

@admin.register(AstroBooking)
class AstroBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at','paid')
    readonly_fields = ('created_at',)

# Register your other models
admin.site.register(Payment)
admin.site.register(Rekhi_Form)
admin.site.register(Report)
