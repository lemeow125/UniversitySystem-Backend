from django.contrib import admin
from enrollment_entries.models import EnrollmentEntry


class EnrollmentEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course')


admin.site.register(EnrollmentEntry, EnrollmentEntryAdmin)
