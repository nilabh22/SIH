from django.contrib import admin
from import_export.admin import ExportActionMixin
from Geeks.models import Department, Details, IndividualForm
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

admin.site.register(Department)
admin.site.register(IndividualForm)

@admin.register(Details)
class DetailAdmin(ImportExportActionModelAdmin):
    pass


