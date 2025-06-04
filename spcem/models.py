from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Owner (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)

class Grave (models.Model):
    class Status (models.TextChoices):
        AVAILABLE = "Available", _("Available")
        RESERVED = "Reserved", _("Reserved")
        OCCUPIED = "Occupied", _("Occupied")

    status = models.CharField(max_length=25, choices=Status, default=Status.AVAILABLE)
    block = models.IntegerField()
    lot = models.IntegerField()
    plot = models.IntegerField()
    owner = models.ForeignKey(Owner, blank=True, null=True, on_delete=models.SET_NULL)

class Deceased (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.CharField(max_length=25, blank=True, null=True)
    dete_of_death = models.CharField(max_length=25, blank=True, null=True)
    grave = models.ForeignKey(Grave, on_delete=models.CASCADE)
