
from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin



@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass


#admin.site.register(Post)
