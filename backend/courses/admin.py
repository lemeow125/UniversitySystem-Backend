from django.contrib import admin
from courses.models import Course


class EnrollmentEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')


admin.site.register(Course, EnrollmentEntryAdmin)
