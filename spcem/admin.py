from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

# Register your models here.
from .models import Owner, Grave, Deceased

class OwnerResource(resources.ModelResource):
    class Meta:
        model = Owner

@admin.register(Owner)
class OwnerAdmin(ImportExportActionModelAdmin):
    resource_classes = [OwnerResource]

class GraveResource(resources.ModelResource):
    class Meta:
        model = Grave

@admin.register(Grave)
class GraveAdmin(ImportExportActionModelAdmin):
    resource_classes = [GraveResource]

class DeceasedResource(resources.ModelResource):
    class Meta:
        model = Owner

@admin.register(Deceased)
class DeceasedAdmin(ImportExportActionModelAdmin):
    resource_classes = [DeceasedResource]

