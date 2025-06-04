from django.urls import path
from . import views

urlpatterns = [
    path("block/", views.BlockView.as_view(), name="block"),
    path("list/", views.BlockListView.as_view(), name="list")
]