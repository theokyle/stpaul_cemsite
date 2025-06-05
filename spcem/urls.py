from django.urls import path
from . import views

urlpatterns = [
    path("block/<int:block_number>/", views.BlockView.as_view(), name="block"),
    path("deceased/create", views.DeceasedCreate.as_view(), name="deceasedcreate")
]