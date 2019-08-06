from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a ingredient')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter the price of this dish.')

    def __str__(self):
        return self.name


class FoodDish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(help_text='Enter a description of this saucer')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter the price of this dish.')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    food_saucer = models.ForeignKey(FoodDish, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4, help_text='Enter the quantity of this dish.')

    def __str__(self):
        return self.food_saucer
