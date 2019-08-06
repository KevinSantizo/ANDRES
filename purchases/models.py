from django.db import models


class Purchase(models.Model):
    quantity = models.IntegerField(help_text='Enter the quantity of food saucers')
