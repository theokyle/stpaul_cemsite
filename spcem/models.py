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

class Block (models.Model):
    number = models.IntegerField()

class Lot (models.Model):
    number = models.IntegerField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE)

class Grave (models.Model):
    class Status (models.TextChoices):
        AVAILABLE = "Available", _("Available")
        RESERVED = "Reserved", _("Reserved")
        OCCUPIED = "Occupied", _("Occupied")

    status = models.CharField(max_length=25, choices=Status, default=Status.AVAILABLE)
    number = models.IntegerField()
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, blank=True, null=True, on_delete=models.SET_NULL)

class Deceased (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.CharField(max_length=25, blank=True, null=True)
    date_of_death = models.CharField(max_length=25, blank=True, null=True)
    grave = models.ForeignKey(Grave, on_delete=models.CASCADE)
