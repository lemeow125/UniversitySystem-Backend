from django.contrib import admin
from curriculums.models import Curriculum


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp')


admin.site.register(Curriculum, CurriculumAdmin)
