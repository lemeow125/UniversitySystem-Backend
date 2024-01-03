from django.contrib import admin
from employment_entries.models import EmploymentEntry


class EmploymentEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'department',
                    'is_professor', 'is_enrollment_staff', 'is_hiring_staff')


admin.site.register(EmploymentEntry, EmploymentEntryAdmin)
