from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView
from .models import Owner, Grave, Deceased

# Create your views here.
class AllBlockView (ListView):
    model = Grave
    template_name = "spcem/block.html"

class BlockView (ListView):
    template_name = "spcem/block.html"

    def get_queryset(self):
        return Grave.objects.filter(block = self.kwargs["block_number"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["block_number"] = self.kwargs["block_number"]
        return context
    
class BlockListView (ListView):
    model = Grave
    template_name = "spcem/list.html"
