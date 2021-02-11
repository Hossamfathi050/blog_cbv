
from django.contrib import admin
from .models import FileAdmin
from import_export.admin import ImportExportModelAdmin



@admin.register(FileAdmin)
class PostImportExport(ImportExportModelAdmin):
    pass


#admin.site.register(Post)