from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Block, Lot, Grave, Deceased
from .forms import DeceasedCreateForm

# Create your views here.
class BlockView (ListView):
    template_name = "spcem/block.html"

    def get_queryset(self):
        self.block = get_object_or_404(Block, number=self.kwargs["block_number"])
        return Lot.objects.filter(block = self.block)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["block_number"] = self.kwargs["block_number"]
        return context

class DeceasedCreate (CreateView):
    model = Deceased
    template_name = 'spcem/deceased_create.html'
    form_class = DeceasedCreateForm