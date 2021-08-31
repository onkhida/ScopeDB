from django.contrib import admin
from .models import (
    Dataset,
    DatasetFile,
    Project
)
admin.site.register(Dataset)
admin.site.register(DatasetFile)
admin.site.register(Project)
