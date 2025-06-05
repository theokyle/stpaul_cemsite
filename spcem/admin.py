from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

# Register your models here.
from .models import Owner, Block, Lot, Grave, Deceased

class OwnerResource(resources.ModelResource):
    class Meta:
        model = Owner

@admin.register(Owner)
class OwnerAdmin(ImportExportActionModelAdmin):
    resource_classes = [OwnerResource]

class BlockResource(resources.ModelResource):
    class Meta:
        model = Block

@admin.register(Block)
class BlockAdmin(ImportExportActionModelAdmin):
    resource_classes = [BlockResource]

class LotResource(resources.ModelResource):
    class Meta:
        model = Lot

@admin.register(Lot)
class LotAdmin(ImportExportActionModelAdmin):
    resource_classes = [LotResource]

class GraveResource(resources.ModelResource):
    class Meta:
        model = Grave

@admin.register(Grave)
class PlotAdmin(ImportExportActionModelAdmin):
    resource_classes = [GraveResource]

class DeceasedResource(resources.ModelResource):
    class Meta:
        model = Deceased

@admin.register(Deceased)
class DeceasedAdmin(ImportExportActionModelAdmin):
    resource_classes = [DeceasedResource]

