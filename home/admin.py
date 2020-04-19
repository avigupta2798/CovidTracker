from django.contrib import admin
from home.models import Covid
# Register your models here.

class CovidAdmin(admin.ModelAdmin):
    search_fields = ['age', 'date_announced', 'city', 'district', 'state', 'gender', 'nationality', 'current_status', 'statecode']
    list_display = ['patient_number', 'age', 'backup_notes', 'current_status', 'date_announced', 'city', 'district', 'state', 'gender', 'nationality', 'notes', 'source1', 'source2', 'source3', 'statecode', 'status_change_date', 'type_of_transmission']
    list_filter = ['age', 'state', 'gender', 'nationality', 'current_status']


admin.site.register(Covid, CovidAdmin)