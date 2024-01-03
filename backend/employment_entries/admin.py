from django.contrib import admin
from employment_entries.models import EmploymentEntry


class EmploymentEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'department')


admin.site.register(EmploymentEntry, EmploymentEntryAdmin)
