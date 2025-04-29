from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerModel(models.Model):
    TheRegion = [
        ('Central','Central'),
        ('East','East'),
        ('West','West'),
    ]

    TheItems = [
        ('Pencil','Pencil'),
        ('Pen','Pen'),
        ('Binder','Binder'),
        ('Desk','Desk'),
        ('Pen Set','Pen Set'),
    ]
    TheDate = models.DateField(auto_now_add=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    Region = models.CharField(choices=TheRegion, max_length=50)
    Rep = models.CharField(max_length=50)
    Items = models.CharField(choices=TheItems, max_length=50)
    Units = models.IntegerField()
    Cost = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return (f'{self.Region} {self.Items} {self.Created_by}')

