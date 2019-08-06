from django.contrib import admin

from stock.models import FoodDish, Ingredient, Recipe


admin.site.register(FoodDish)
admin.site.register(Ingredient)
admin.site.register(Recipe)
