from django.shortcuts import render, HttpResponse, \
    HttpResponseRedirect, reverse

from users.models import User


def render_register_user(request):
    template = 'users/register_user.html'
    return render(request, template)


def process_register_user(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        new_user.save()

        return HttpResponseRedirect(reverse('users:login'))
    return HttpResponse('Error: method not allowed.')


def render_login(request):
    template = 'users/login.html'
    return render(request, template)


def process_login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'],
                                    password=request.POST['password'])
        except User.DoesNotExist:
            return HttpResponse('User does not exist.')

        return HttpResponseRedirect(reverse('stock:menu',
                                            kwargs={'user_pk': user.pk}))
    return HttpResponse('Error: method not allowed')
