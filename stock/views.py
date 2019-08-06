from django.shortcuts import render, HttpResponse, \
    HttpResponseRedirect, reverse

from stock.models import FoodDish, Ingredient


def create_dish(request):
    template = 'stock/create_dish.html'
    context = {
        'dishes': FoodDish.objects.all(),
        'ingredients': Ingredient.objects.all()
    }
    return render(request, template, context)


def process_create_dish(request):
    if request.method == 'POST':
        new_dish = FoodDish(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            image=request.POST['image'],
        )
        new_dish.save()

        return HttpResponseRedirect(reverse('stock:menu', kwargs={'user_pk': new_dish.owner.id}))
    return HttpResponse('Error: method not allowed.')


def create_ingredient(request):
    template = 'stock/create_ingredient.html'
    context = {
        'dishes': FoodDish.objects.all(),
        'ingredients': Ingredient.objects.all()
    }
    return render(request, template, context)


def process_create_ingredient(request):
    if request.method == 'POST':
        new_dish = FoodDish(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            image=request.POST['image'],
        )
        new_dish.save()

        return HttpResponseRedirect(reverse('stock:menu', kwargs={'user_pk': new_dish.owner.id}))
    return HttpResponse('Error: method not allowed.')


def menu(request, user_pk):
    template = 'stock/menu.html'
    context = {
        'food_saucers': FoodDish.objects.all(),
        'user': user_pk
    }
    return render(request, template, context)


def pre_purchases(request, user_pk):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('purchases:pay', kwargs={'user_pk': user_pk}))
    return HttpResponse('Error: method not allowed.')

