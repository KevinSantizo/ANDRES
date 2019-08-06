from django.shortcuts import render


def render_purchase(request):
    template = 'purchases/purchase.html'
    return render(request, template)
