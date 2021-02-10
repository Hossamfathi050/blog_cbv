
from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin



@
admin.site.register(Post)
