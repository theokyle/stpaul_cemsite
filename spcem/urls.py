from django.urls import path
from . import views

urlpatterns = [
    path("block/", views.AllBlockView.as_view(), name="all_block"),
    path("block/<int:block_number>/", views.BlockView.as_view(), name="block"),
    path("list/", views.BlockListView.as_view(), name="list")
]