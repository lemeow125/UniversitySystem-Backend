from django.contrib import admin
from departments.models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp')


admin.site.register(Department, DepartmentAdmin)
