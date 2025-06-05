from django import forms
from .models import Block, Lot, Grave, Deceased

class DeceasedCreateForm(forms.ModelForm):
    class Meta:
        model = Deceased
        fields = ("first_name", "last_name", "date_of_birth", "date_of_death")