from django.shortcuts import render
from django.views.generic import ListView
from .models import Owner, Grave, Deceased

# Create your views here.
class BlockView (ListView):
    model = Grave
    template_name = "spcem/block.html"

class BlockListView (ListView):
    model = Grave
    template_name = "spcem/list.html"
